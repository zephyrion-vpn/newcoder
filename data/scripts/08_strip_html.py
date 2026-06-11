import re

TAG_PATTERN = re.compile(r"<[^>]+>")
WHITESPACE_PATTERN = re.compile(r"\s+")


def strip_html(html: str) -> str:
    without_tags = TAG_PATTERN.sub(" ", html)
    return WHITESPACE_PATTERN.sub(" ", without_tags).strip()


def main() -> None:
    html = "<p>Привет, <b>мир</b>!</p><br><div>Как <i>дела</i>?</div>"
    print(strip_html(html))


if __name__ == "__main__":
    main()
