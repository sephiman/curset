import { Prose } from "@/lib/markdown";

const HAS_CODE = /`[^`\n]+`/;

/** An option's words; one that holds code (`inline` or fenced) is read as markdown, any other stays plain text. */
export function OptionText({ text }: { text: string }) {
  if (!HAS_CODE.test(text)) return <span>{text}</span>;
  return (
    <span className="block min-w-0 [&_p]:my-0 [&_pre]:my-1">
      <Prose markdown={text} />
    </span>
  );
}
