# SPDX-License-Identifier: AGPL-3.0-only
"""Technical-documentation sources of a course (`sources/sources.yaml`): fetch, register, split into anchors.

    uv run python scripts/tech_sources.py fetch --course backend-in-depth --id ID --url URL \
        --tier A --product P --version V --title T [--kind html|pdf] [--evidence]
    uv run python scripts/tech_sources.py anchors --course backend-in-depth [--id ID ...]
    uv run python scripts/tech_sources.py show --course backend-in-depth SOURCE_ID#ANCHOR
    uv run python scripts/tech_sources.py list --course backend-in-depth SOURCE_ID
    uv run python scripts/tech_sources.py apply-licences --course backend-in-depth

`fetch` tries a plain HTTP GET and falls back to headless Chromium (Playwright from frontend/node_modules)
when the site refuses or serves a script shell. HTML is stored stripped (scripts/strip_saved_pages.py rules);
the bytes as fetched go to ~/PycharmProjects/curset-saved-originals/<course>/, out of git. A new entry is
registered with the licence of its `sources/licences.yaml` rule (none: `pending`); a copy whose rule does not
allow extracts is kept outside git (`storage: local`, under the originals folder) with its sha256 and anchors.
"""

from __future__ import annotations

import argparse
import fcntl
import json
import re
import subprocess
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tradeschool.citations.saved_pages import strip_page

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "content"
ORIGINALS = Path.home() / "PycharmProjects" / "curset-saved-originals"
RENDER_SCRIPT = Path(__file__).resolve().parent / "fetch_rendered.cjs"
HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}
#: Paragraph classes that act as headings: EUR-Lex article titles (the article id is on the enclosing div).
HEADING_CLASSES = {"oj-ti-art": 3}
SKIPPED = {"script", "style", "nav", "noscript", "template", "svg"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
#: A page whose visible text is shorter than this is taken to be a script shell and is rendered instead.
MIN_TEXT_CHARS = 1500
SOURCES_HEADER = (
    "# SPDX-License-Identifier: AGPL-3.0-only\n"
    "# Sources of this course (requirements section 3.2). Written by scripts/tech_sources.py; licence\n"
    "# fields by the S0 licence check. Anchors: sources/anchors/<id>.json (generated).\n"
    "# Files: sources/docs/ (not served to readers).\n"
)


@dataclass(frozen=True)
class Anchor:
    anchor: str
    title: str
    level: int
    text: str

    @property
    def digest(self) -> str:
        return sha256(self.text.encode("utf-8")).hexdigest()


class _AnchorParser(HTMLParser):
    """Cuts a page at every heading; each cut takes the heading's id, an id inside it, or its section's id."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.anchors: list[Anchor] = []
        self._stack: list[tuple[str, str | None, bool]] = []
        self._after_heading = False
        self._heading_tag = ""
        self._ids_since_heading: list[str] = []
        self._current = Anchor("top", "", 0, "")
        self._parts: list[str] = []
        self._heading: tuple[int, str | None, list[str]] | None = None

    @property
    def _skipping(self) -> bool:
        return any(skipped for _, _, skipped in self._stack)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        found = dict(attrs)
        ident = found.get("id") or (found.get("name") if tag == "a" else None)
        skipped = tag in SKIPPED or found.get("role") == "navigation"
        if tag not in VOID:
            self._stack.append((tag, ident, skipped))
        if self._skipping:
            return
        if self._after_heading and ident and ident.startswith("user-content-"):
            # GitHub markdown: the permalink <a id> follows the heading instead of sitting inside it
            current = self._current
            self._current = Anchor(ident.removeprefix("user-content-"), current.title, current.level, "")
            self._after_heading = False
            return
        heading_class = HEADING_CLASSES.get(found.get("class") or "")
        if tag in HEADINGS or heading_class:
            self._heading = (HEADINGS.get(tag) or heading_class or 0, ident, [])
            self._heading_tag = tag
        elif ident and self._heading is not None and self._heading[1] is None:
            self._heading = (self._heading[0], ident, self._heading[2])
        elif ident:
            self._ids_since_heading.append(ident)
        if tag in {"p", "div", "li", "tr", "pre", "section", "br", "dt", "dd", "table", "blockquote"}:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID or all(open_tag != tag for open_tag, _, _ in self._stack):
            return  # a stray end tag closes nothing, as in a browser
        while self._stack and self._stack.pop()[0] != tag:
            pass
        if tag == self._heading_tag and self._heading is not None:
            self._close_heading()
        elif tag in {"p", "div", "li", "tr", "pre", "td", "th"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skipping:
            return
        if data.strip():
            self._after_heading = False
        if not any(tag == "pre" for tag, _, _ in self._stack):
            data = re.sub(r"\s+", " ", data)  # source line breaks are not text breaks outside <pre>
        if self._heading is not None:
            self._heading[2].append(data)
        else:
            self._parts.append(data)

    def _close_heading(self) -> None:
        assert self._heading is not None
        level, ident, words = self._heading
        title = _collapse(" ".join(words))
        self._heading = None
        self._flush()
        container = self._ids_since_heading[-1] if self._ids_since_heading else None
        if container and self._heading_tag not in HEADINGS:
            ident = container  # a class-marked title: the enclosing division carries the citable id
        if ident and ident.startswith("name-") and container and container.startswith("section-"):
            ident = container  # xml2rfc: the section id is the citable one, the heading id is a slug
        name = ident or container or _slug(title)
        self._current = Anchor(name, title, level, "")
        self._parts = [title, "\n"]
        self._ids_since_heading = []
        self._after_heading = True

    def _flush(self) -> None:
        text = _normalise("".join(self._parts))
        if text or self._current.anchor != "top":
            self.anchors.append(Anchor(self._current.anchor, self._current.title, self._current.level, text))

    def finish(self) -> list[Anchor]:
        self.close()
        self._flush()
        return _deduplicated(self.anchors)


def _collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _normalise(text: str) -> str:
    lines = (_collapse(line) for line in text.split("\n"))
    return "\n".join(line for line in lines if line)


def _slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "untitled"


def _deduplicated(anchors: list[Anchor]) -> list[Anchor]:
    seen: dict[str, int] = {}
    out: list[Anchor] = []
    for a in anchors:
        count = seen.get(a.anchor, 0) + 1
        seen[a.anchor] = count
        out.append(a if count == 1 else Anchor(f"{a.anchor}~{count}", a.title, a.level, a.text))
    return out


def html_anchors(html: str) -> list[Anchor]:
    parser = _AnchorParser()
    parser.feed(html)
    return parser.finish()


def pdf_anchors(path: Path) -> list[Anchor]:
    """One anchor per page, `p<N>`."""
    command = ["pdftotext", "-layout", str(path), "-"]
    text = subprocess.run(command, capture_output=True, check=True, text=True)
    pages = enumerate(text.stdout.split("\f"), 1)
    return [Anchor(f"p{n}", f"page {n}", 0, _normalise(page)) for n, page in pages if page.strip()]


def visible_text_chars(html: bytes) -> int:
    return sum(len(a.text) for a in html_anchors(html.decode("utf-8", errors="replace")))


# --- fetch ---------------------------------------------------------------------------------------------


def plain_fetch(url: str) -> bytes | None:
    """curl with its own defaults: no browser headers."""
    result = subprocess.run(["curl", "-sSfL", "--compressed", "--max-time", "90", url], capture_output=True)
    if result.returncode != 0:
        print(f"plain fetch failed: {result.stderr.decode(errors='replace').strip()}", file=sys.stderr)
        return None
    return result.stdout


def rendered_fetch(url: str) -> bytes:
    result = subprocess.run(
        ["node", str(RENDER_SCRIPT), url], capture_output=True, check=True, cwd=REPO / "frontend", timeout=180
    )
    return result.stdout


@contextmanager
def locked(path: Path) -> Iterator[None]:
    lock = path.with_suffix(".lock")
    with lock.open("w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def read_registry(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    entries: list[dict[str, object]] = loaded.get("sources", [])
    return entries


def write_registry(path: Path, entries: list[dict[str, object]]) -> None:
    ordered = sorted(entries, key=lambda e: str(e["id"]))
    body = yaml.safe_dump({"sources": ordered}, sort_keys=False, allow_unicode=True, width=120)
    path.write_text(SOURCES_HEADER + body, encoding="utf-8")


def fetch(args: argparse.Namespace) -> None:
    sources = CONTENT / args.course / "sources"
    kind = args.kind or ("pdf" if args.url.lower().endswith(".pdf") else "html")
    folder = "evidence" if args.evidence else "docs"
    target = sources / folder / f"{args.id}.{kind}"
    raw = plain_fetch(args.url)
    method = "plain"
    if kind == "html" and (raw is None or visible_text_chars(raw) < MIN_TEXT_CHARS):
        raw = rendered_fetch(args.url)
        method = "playwright"
    if raw is None:
        raise SystemExit(f"{args.id}: no bytes from {args.url}")
    original = ORIGINALS / args.course / folder / target.name
    original.parent.mkdir(parents=True, exist_ok=True)
    original.write_bytes(raw)
    stored = strip_page(raw) if kind == "html" else raw
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(stored)
    digest = sha256(stored).hexdigest()
    entry: dict[str, object] = {
        "id": args.id,
        "tier": "evidence" if args.evidence else args.tier,
        "product": args.product,
        "version": args.version,
        "title": args.title,
        "url": args.url,
        "retrieved": date.today().isoformat(),
        "method": method,
        "sha256": digest,
        "path": str(target.relative_to(CONTENT / args.course)),
        "licence": "pending",
        "extract_allowed": False,
    }
    registry = sources / ("evidence.yaml" if args.evidence else "sources.yaml")
    with locked(registry):
        current = read_registry(registry)
        entries = [e for e in current if e["id"] != args.id]
        previous = next((e for e in current if e["id"] == args.id), None)
        if previous is not None and previous.get("storage") == "local":
            stale = _resolve(args.course, previous)
            if stale != target:
                stale.unlink(missing_ok=True)
        _place(args.course, entry, licence_rules(sources))
        write_registry(registry, [*entries, entry])
    if not args.evidence:
        write_anchors(sources, args.id, _resolve(args.course, entry))
    print(f"{args.id}: {method}, {len(stored)} bytes, sha256 {digest[:12]}")


# --- anchors -------------------------------------------------------------------------------------------


def anchors_of(path: Path) -> list[Anchor]:
    if path.suffix == ".pdf":
        return pdf_anchors(path)
    return html_anchors(path.read_text(encoding="utf-8", errors="replace"))


def write_anchors(sources: Path, source_id: str, path: Path) -> int:
    found = anchors_of(path)
    rows = [{"anchor": a.anchor, "title": a.title, "level": a.level, "sha256": a.digest} for a in found]
    out = sources / "anchors" / f"{source_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"source": source_id, "anchors": rows}, indent=1, ensure_ascii=False) + "\n")
    return len(rows)


def rebuild_anchors(args: argparse.Namespace) -> None:
    sources = CONTENT / args.course / "sources"
    for entry in read_registry(sources / "sources.yaml"):
        if args.id and entry["id"] not in args.id:
            continue
        count = write_anchors(sources, str(entry["id"]), _resolve(args.course, entry))
        print(f"{entry['id']}: {count} anchors")


def _source_path(course: str, source_id: str) -> Path:
    sources = CONTENT / course / "sources"
    registered = read_registry(sources / "sources.yaml") + read_registry(sources / "evidence.yaml")
    entries = {e["id"]: e for e in registered}
    if source_id not in entries:
        raise SystemExit(f"unknown source {source_id}")
    return _resolve(course, entries[source_id])


def show(args: argparse.Namespace) -> None:
    source_id, _, name = args.ref.partition("#")
    for a in anchors_of(_source_path(args.course, source_id)):
        if a.anchor == name:
            print(f"[{source_id}#{a.anchor}] sha256 {a.digest}\n{a.text}")
            return
    raise SystemExit(f"no anchor {name!r} in {source_id}")


def list_anchors(args: argparse.Namespace) -> None:
    for a in anchors_of(_source_path(args.course, args.source)):
        print(f"{a.anchor}\t{len(a.text)}\t{a.title}")


def _licence_for(url: str, rules: list[dict[str, object]]) -> dict[str, object] | None:
    """The rule whose `prefix` is the longest prefix of the URL without its scheme."""
    bare = re.sub(r"^https?://(www\.)?", "", url)
    matches = [r for r in rules if bare.startswith(str(r["prefix"]))]
    return max(matches, key=lambda r: len(str(r["prefix"])), default=None)


def licence_rules(sources: Path) -> list[dict[str, object]]:
    path = sources / "licences.yaml"
    if not path.exists():
        return []
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rules: list[dict[str, object]] = loaded.get("licences", [])
    return rules


def _resolve(course: str, entry: dict[str, object]) -> Path:
    """A `storage: local` copy lives outside git: its terms do not clearly allow redistribution."""
    if entry.get("storage") == "local":
        return ORIGINALS / course / "local" / str(entry["path"])
    return CONTENT / course / str(entry["path"])


def _place(course: str, entry: dict[str, object], rules: list[dict[str, object]]) -> bool:
    """Licence fields from the matching rule, the copy moved to match; False when no rule matches."""
    before = _resolve(course, entry)
    rule = _licence_for(str(entry["url"]), rules)
    entry["licence"] = rule["licence"] if rule else "pending"
    entry["extract_allowed"] = bool(rule["extract_allowed"]) if rule else False
    entry["storage"] = "repo" if entry["extract_allowed"] else "local"
    after = _resolve(course, entry)
    if before != after and before.exists():
        after.parent.mkdir(parents=True, exist_ok=True)
        before.replace(after)
    return rule is not None


def apply_licences(args: argparse.Namespace) -> None:
    sources = CONTENT / args.course / "sources"
    rules = licence_rules(sources)
    unmatched: set[str] = set()
    counts = {"repo": 0, "local": 0}
    for name in ("sources.yaml", "evidence.yaml"):
        registry = sources / name
        with locked(registry):
            entries = read_registry(registry)
            for entry in entries:
                if not _place(args.course, entry, rules):
                    unmatched.add(re.sub(r"^https?://(www\.)?([^/]+).*", r"\2", str(entry["url"])))
                counts[str(entry["storage"])] += 1
            write_registry(registry, entries)
    missing = sorted(unmatched) or "none"
    print(f"in repo {counts['repo']}, local only {counts['local']}; hosts without a licence rule: {missing}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    commands = parser.add_subparsers(dest="command", required=True)
    f = commands.add_parser("fetch")
    f.add_argument("--course", required=True)
    f.add_argument("--id", required=True)
    f.add_argument("--url", required=True)
    f.add_argument("--tier", choices=["A", "C", "evidence"], default="A")
    f.add_argument("--product", required=True)
    f.add_argument("--version", required=True)
    f.add_argument("--title", required=True)
    f.add_argument("--kind", choices=["html", "pdf"])
    f.add_argument("--evidence", action="store_true", help="a page that states a version, kept apart")
    f.set_defaults(run=fetch)
    a = commands.add_parser("anchors")
    a.add_argument("--course", required=True)
    a.add_argument("--id", nargs="*")
    a.set_defaults(run=rebuild_anchors)
    s = commands.add_parser("show")
    s.add_argument("--course", required=True)
    s.add_argument("ref")
    s.set_defaults(run=show)
    lst = commands.add_parser("list")
    lst.add_argument("--course", required=True)
    lst.add_argument("source")
    lst.set_defaults(run=list_anchors)
    lic = commands.add_parser("apply-licences")
    lic.add_argument("--course", required=True)
    lic.set_defaults(run=apply_licences)
    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
