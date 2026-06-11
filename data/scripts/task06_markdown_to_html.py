import html
import re
import sys
from pathlib import Path

_HEADING = re.compile(r"(#{1,6})\s+(.*)")
_INLINE_RULES = (
    (re.compile(r"\*\*(.+?)\*\*"), r"<b>\1</b>"),
    (re.compile(r"\*(.+?)\*"), r"<i>\1</i>"),
    (re.compile(r"`(.+?)`"), r"<code>\1</code>"),
)


def _apply_inline(text: str) -> str:
    for pattern, replacement in _INLINE_RULES:
        text = pattern.sub(replacement, text)
    return text


def markdown_to_html(markdown: str) -> str:
    blocks: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        heading = _HEADING.fullmatch(stripped)
        if heading:
            level = len(heading.group(1))
            content = _apply_inline(html.escape(heading.group(2)))
            blocks.append(f"<h{level}>{content}</h{level}>")
        else:
            blocks.append(f"<p>{_apply_inline(html.escape(stripped))}</p>")
    return "\n".join(blocks)


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Использование: {Path(sys.argv[0]).name} <файл.md>", file=sys.stderr)
        raise SystemExit(2)
    source = Path(sys.argv[1])
    if not source.is_file():
        print(f"Файл не найден: {source}", file=sys.stderr)
        raise SystemExit(1)
    output = source.with_suffix(".html")
    output.write_text(markdown_to_html(source.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"HTML сохранён: {output.resolve()}")


if __name__ == "__main__":
    main()
