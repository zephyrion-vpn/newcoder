import re
import tempfile
from pathlib import Path


def inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def convert_line(line: str) -> str:
    heading = re.match(r"^(#{1,6})\s+(.*)$", line)
    if heading:
        level = len(heading.group(1))
        return f"<h{level}>{inline(heading.group(2))}</h{level}>"
    if line.strip() == "":
        return ""
    return f"<p>{inline(line)}</p>"


def markdown_to_html(markdown: str) -> str:
    lines = [convert_line(line) for line in markdown.splitlines()]
    return "\n".join(line for line in lines if line)


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    md_path = tmp / "doc.md"
    markdown = (
        "# Заголовок\n"
        "## Подзаголовок\n"
        "Это **жирный** и *курсивный* текст.\n"
        "Ссылка: [пример](https://example.com) и `code`.\n"
    )
    md_path.write_text(markdown, encoding="utf-8")

    html = markdown_to_html(md_path.read_text(encoding="utf-8"))
    (tmp / "doc.html").write_text(html, encoding="utf-8")
    print("HTML:")
    print(html)


if __name__ == "__main__":
    main()
