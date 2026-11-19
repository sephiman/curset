"""select_lesson.py <lesson…>: assemble a lesson from the pool within its budget.

Priority (edition step 1): a official-question sentences and esquemas · b concept readers' picks (edition/b/<lesson>.json)
· c R2b restores and confirmed review items · d «No confundir» notes and the estimación objetiva paragraph · e esquemas
that gather two or more cited articles of kept content (rows are free) · f remaining pre-R2d sentences by exam weight.
Whole sentences only, byte-identical; a, b, c are never cut; a lead-in that ends in «:» comes with its list or esquema.
Writes the lesson in place, edition/selection/<lesson>.json and reserve/<lesson>.md.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lesson_model import ROOT, Block, Lesson, key, parse, rebuild, references, words  # noqa: E402

AEAT = ROOT / "docs/age-verification/aeat"
EDITION = AEAT / "edition"
CONTENT = ROOT / "content/aeat-agentes-hacienda/es/lessons"
DERIVED = ("Lo que más cae", "Normativa")
ESTIMACION = "Los contribuyentes que reúnan las circunstancias previstas en las normas reguladoras de la estimación objetiva"


def cite_keys(text: str, fine: bool = False) -> set[str]:
    """«168 CE» (article) or «168.1 CE» (fine) keys of the article references in a text; ranges expanded."""
    keys: set[str] = set()
    for body, norm in references(text):
        for a, b in re.findall(r"(\d+)\s*(?:\N{EN DASH}|-|to|a)\s*(\d+)", body):
            if int(b) - int(a) < 300:
                keys.update(f"{n} {norm}" for n in range(int(a), int(b) + 1))
        for token in (m.group(0) for t in body.split() if (m := re.match(r"\d+(?:\.\d+)?", t))):
            keys.add(f"{token if fine else token.split('.')[0]} {norm}")
    return keys


def load_tags(lesson: str) -> dict[str, dict[str, str]]:
    rows = json.loads((AEAT / "r2d/tags" / f"{lesson}.json").read_text())
    return {r["id"]: r for r in rows}


class Selection:
    def __init__(self, lesson: str, budget: int) -> None:
        self.lesson = lesson
        self.text = (AEAT / "pool" / f"{lesson}.md").read_text()
        self.model: Lesson = parse(self.text)
        self.tags = load_tags(lesson)
        self.budget = budget
        cov = json.loads((EDITION / "coverage-a.json").read_text()).get(lesson, {})
        self.a_ids = {i for info in cov.values() for i in info["sentences"]}
        self.a_esq = {i for info in cov.values() for i in info["esquemas"]}
        bpath = EDITION / "b" / f"{lesson}.json"
        data = json.loads(bpath.read_text()) if bpath.exists() else {}
        self.picks: list[dict[str, object]] = data.get("picks", [])
        self.b_esquemas: set[int] = {int(re.sub(r"\D", "", str(x["index"]))) for x in data.get("esquemas", [])}
        self.restore_ids: set[str] = set()
        self.restore_esq: set[int] = set()
        for name in ("bank", "reader", "anchors"):
            rpath = EDITION / "restore" / f"{lesson}.{name}.json"
            if rpath.exists():
                rdata = json.loads(rpath.read_text())
                self.restore_ids |= set(rdata.get("sentences", []))
                self.restore_esq |= {int(x) for x in rdata.get("esquemas", [])}
        swap_path = EDITION / "swap.json"
        self.swap: dict[str, str] = json.loads(swap_path.read_text()).get(lesson, {}) if swap_path.exists() else {}
        self.drop_esq: set[int] = set()
        apath = EDITION / "restore" / f"{lesson}.anchors.json"
        if apath.exists():
            self.drop_esq = {int(x) for x in json.loads(apath.read_text()).get("drop_esquemas", [])}
        self.asked_keys: set[str] = set()
        info = json.loads((EDITION / "budget.json").read_text())[lesson]["asked"]
        for cite in info.values():
            self.asked_keys |= cite_keys(cite if cite.startswith("art") else "arts. " + cite)
        self.cls: dict[tuple[int, str], str] = {}
        self.esq_cls: dict[int, str] = {}
        self.derived_sections = self._derived_sections()
        self.atomic = self._atomic_blocks()
        self.all: list = [(b, s) for b in self.model.blocks for s in b.sentences if b.section not in self.derived_sections]

    def _derived_sections(self) -> set[int]:
        out: set[int] = set()
        for sec in self.model.sections:
            if sec.title in DERIVED:
                out.add(sec.index)
        return out

    def _atomic_blocks(self) -> set[int]:
        atomic: set[int] = set()
        for b in self.model.blocks:
            multi = len(b.sentences) > 1
            nested = any(line.startswith(" ") for line in self.model.lines[b.first - 1 : b.last])
            if b.kind == "item" and multi and nested:
                atomic.add(b.sentences[0].block)
        return atomic

    # -- helpers -------------------------------------------------------------------------------------------
    def origin(self, s) -> str:
        return self.tags.get(s.id, {}).get("origin", "reworded")

    def words_kept(self) -> int:
        return sum(words(s.text) for b, s in self.all if key(s) in self.cls)

    def take(self, b: Block, s, label: str) -> None:
        group = b.sentences if (s.block in self.atomic or b.note is not None) else [s]
        for g in group:
            self.cls.setdefault(key(g), label)

    def leadin(self, b: Block) -> None:
        """A kept list item or esquema comes with the paragraph that ends in «:» just before it."""
        blocks = [x for x in self.model.blocks if x.section == b.section]
        index = blocks.index(b)
        while index > 0 and blocks[index].kind == "item":
            index -= 1
        head = blocks[index]
        if head.kind != "item" and head.sentences[-1].text.rstrip().endswith(":") and head is not b:
            self.cls.setdefault(key(head.sentences[-1]), "lead-in")

    def esquema_leadin(self, i: int) -> None:
        e = self.model.esquemas[i]
        before = [b for b in self.model.blocks if b.last < e.first and b.section == e.section and b.note is None]
        if before and before[-1].last >= e.first - 3 and before[-1].sentences[-1].text.rstrip().endswith(":"):
            self.cls.setdefault(key(before[-1].sentences[-1]), "lead-in")

    # -- passes --------------------------------------------------------------------------------------------
    def run(self) -> None:
        for b, s in self.all:
            if s.id in self.a_ids:
                self.take(b, s, "a")
            elif s.id in self.restore_ids:
                self.take(b, s, "restore")
            elif s.id in self.swap:
                self.take(b, s, "xref")
        self.a_esq_kept = set(self.a_esq)
        by_id = {s.id: (b, s) for b, s in self.all}
        for pick in self.picks:
            hit = by_id.get(str(pick["id"]))
            if hit and int(pick.get("rank", 1)) <= 2:
                self.take(hit[0], hit[1], "b")
        for b, s in self.all:
            if self.origin(s) in ("R2b restore", "review item"):
                self.take(b, s, "c")
        for b, s in self.all:
            if b.kind == "paragraph" and s.text.startswith(ESTIMACION):
                for g in b.sentences:
                    self.cls.setdefault(key(g), "d")
        # notes are units: a kept sentence in a «No confundir» note brings the whole note
        for i, note in enumerate(self.model.notes):
            if note.type != "warning":
                continue
            inside = [(b, s) for b, s in self.all if b.note == i]
            if any(key(s) in self.cls for _, s in inside):
                for _, s in inside:
                    self.cls.setdefault(key(s), "d")
        for i, note in enumerate(self.model.notes):
            if note.type != "warning":
                continue
            inside = [(b, s) for b, s in self.all if b.note == i]
            cost = sum(words(s.text) for _, s in inside)
            if not any(key(s) in self.cls for _, s in inside) and self.words_kept() + cost <= self.budget:
                for _, s in inside:
                    self.cls[key(s)] = "d"
        self.choose_esquemas()
        # b rank 3 («nice to have»): only while the budget lasts, before f
        for pick in self.picks:
            hit = by_id.get(str(pick["id"]))
            if hit and int(pick.get("rank", 1)) > 2 and key(hit[1]) not in self.cls:
                group = hit[0].sentences if hit[1].block in self.atomic or hit[0].note is not None else [hit[1]]
                if self.words_kept() + sum(words(g.text) for g in group) <= self.budget:
                    for g in group:
                        self.cls.setdefault(key(g), "b3")
        # f: remaining pre-R2d sentences by exam weight
        order = {key(s): n for n, (b, s) in enumerate(self.all)}
        pool_f = [(b, s) for b, s in self.all if key(s) not in self.cls and self.origin(s) == "HEAD" and b.note is None]
        sections_with_a = {b.section for b, s in self.all if self.cls.get(key(s)) == "a"}

        def weight(item) -> tuple[float, int]:
            b, s = item
            hits = len(cite_keys(s.text) & self.asked_keys)
            return (-(hits + (0.5 if b.section in sections_with_a else 0.0)), order[key(s)])

        for b, s in sorted(pool_f, key=weight):
            group = [g for g in (b.sentences if s.block in self.atomic else [s]) if key(g) not in self.cls]
            cost = sum(words(g.text) for g in group)
            if self.words_kept() + cost <= self.budget:
                for g in group:
                    self.cls[key(g)] = "f"
        self.choose_esquemas()
        # lead-ins of kept items
        for b, s in self.all:
            if key(s) in self.cls and b.kind == "item":
                self.leadin(b)
        for i in self.esq_cls:
            self.esquema_leadin(i)
        self.items_of_leadins()
        self.info_notes()

    def items_of_leadins(self) -> None:
        """A kept sentence that ends in «:» brings the esquema or the list items that follow it."""
        blocks = self.model.blocks
        for b, s in list(self.all):
            if key(s) not in self.cls or not s.text.rstrip().endswith(":") or b.sentences[-1] is not s:
                continue
            for i, e in enumerate(self.model.esquemas):
                if b.last < e.first <= b.last + 3 and i not in self.esq_cls:
                    self.esq_cls[i] = "e"
            index = blocks.index(b)
            run = []
            for nxt in blocks[index + 1 :]:
                if nxt.kind != "item" or nxt.first > (run[-1].last if run else b.last) + 2:
                    break
                run.append(nxt)
            if run and not any(key(x) in self.cls for blk in run for x in blk.sentences):
                for blk in run:
                    for x in blk.sentences:
                        self.cls.setdefault(key(x), "items")

    def choose_esquemas(self) -> None:
        kept_cites: set[str] = set()
        for b, s in self.all:
            if key(s) in self.cls:
                kept_cites |= cite_keys(s.text, fine=True)
        for i, e in enumerate(self.model.esquemas):
            if i in self.esq_cls or (i in self.drop_esq and i not in self.a_esq):
                continue
            if i in self.a_esq:
                self.esq_cls[i] = "a"
                continue
            if i in self.restore_esq:
                self.esq_cls[i] = "restore"
                continue
            if i in self.b_esquemas:
                self.esq_cls[i] = "b"
                continue
            rows = " ".join(s.text for s in e.sentences)
            cites = cite_keys(rows, fine=True)
            gathered = cites & kept_cites
            articles = {c.split(".")[0] + " " + c.split(" ", 1)[1] for c in cites}
            if len(cites) >= 2 and len(articles | set()) >= 1 and len(gathered) >= 2:
                self.esq_cls[i] = "e"

    def info_notes(self) -> None:
        """A «Fuera del enunciado literal» note stays when the content right after it stays."""
        self.kept_notes: set[int] = set()
        for i, note in enumerate(self.model.notes):
            if note.type != "info":
                continue
            after = [b for b in self.model.blocks if b.first > note.last and b.note is None]
            esq_after = [(j, e) for j, e in enumerate(self.model.esquemas) if e.first > note.last]
            nxt_block = after[0] if after else None
            nxt_esq = esq_after[0] if esq_after else None
            first_is_esq = nxt_esq and (not nxt_block or nxt_esq[1].first < nxt_block.first)
            if first_is_esq:
                kept = nxt_esq[0] in self.esq_cls  # type: ignore[index]
            else:
                kept = bool(nxt_block) and any(key(s) in self.cls for s in nxt_block.sentences)  # type: ignore[union-attr]
            if kept:
                for b in self.model.blocks:
                    if b.note == i:
                        for s in b.sentences:
                            self.cls[key(s)] = "note"

    # -- derived sections --------------------------------------------------------------------------------
    def derived_keep(self) -> set[tuple[int, str]]:
        kept_cites: set[str] = set()
        for b, s in self.all:
            if key(s) in self.cls:
                kept_cites |= cite_keys(s.text, fine=True)
        for i in self.esq_cls:
            kept_cites |= cite_keys(" ".join(s.text for s in self.model.esquemas[i].sentences), fine=True)
        out: set[tuple[int, str]] = set()
        for b in self.model.blocks:
            if self.model.sections[b.section].title != "Lo que más cae":
                continue
            for s in b.sentences:
                needed = cite_keys(s.text, fine=True)
                if s.id in self.a_ids or s.id in self.restore_ids or (needed and needed <= kept_cites):
                    out.add(key(s))
        return out


def assemble(lesson: str, budget: int) -> tuple[Selection, str, set[tuple[int, str]]]:
    sel = Selection(lesson, budget)
    sel.run()
    derived = sel.derived_keep()
    derived_words = sum(words(s.text) for b in sel.model.blocks for s in b.sentences if key(s) in derived)
    if derived_words:
        sel2 = Selection(lesson, max(budget - derived_words, 0))
        sel2.run()
        derived2 = sel2.derived_keep()
        # a, b, c can overrun the reduced budget: they are never cut, so the derived layer may only shrink
        sel, derived = sel2, derived2
    keep = set(sel.cls) | derived
    text = rebuild(sel.model, keep, set(sel.esq_cls), sel.swap)
    return sel, text, derived


def main(argv: list[str]) -> int:
    table = json.loads((EDITION / "budget.json").read_text())
    lessons = argv or [x for x in table if x != "m00-l01"]
    (EDITION / "selection").mkdir(exist_ok=True)
    for lesson in lessons:
        sel, text, derived = assemble(lesson, int(table[lesson]["budget"]))
        counts: dict[str, int] = {}
        wc: dict[str, int] = {}
        for k, label in sel.cls.items():
            counts[label] = counts.get(label, 0) + 1
        for b, s in sel.all:
            if key(s) in sel.cls:
                wc[sel.cls[key(s)]] = wc.get(sel.cls[key(s)], 0) + words(s.text)
        total = sum(wc.values())
        info = {
            "lesson": lesson,
            "budget": table[lesson]["budget"],
            "words_body": total,
            "words_derived": sum(words(s.text) for b in sel.model.blocks for s in b.sentences if key(s) in derived),
            "by_class_sentences": counts,
            "by_class_words": wc,
            "esquemas": {c: sum(1 for v in sel.esq_cls.values() if v == c) for c in {"a", "e"}},
            "esquemas_total": len(sel.model.esquemas),
            "sentences_total": len(sel.all),
        }
        (EDITION / "selection" / f"{lesson}.json").write_text(json.dumps(info, ensure_ascii=False, indent=1) + "\n")
        (EDITION / "selection" / f"{lesson}.text").write_text(text)
        print(lesson, json.dumps({k: info[k] for k in ("budget", "words_body", "words_derived", "by_class_words")}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
