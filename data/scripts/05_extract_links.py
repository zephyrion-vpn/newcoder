import re

HREF_PATTERN = re.compile(r"<a\b[^>]*?\bhref\s*=\s*[\"']([^\"']*)[\"']", re.IGNORECASE)


def extract_links(html: str) -> list[str]:
    return HREF_PATTERN.findall(html)


def main() -> None:
    html = (
        '<a href="https://example.com">Пример</a> текст '
        "<a class='x' href='/page'>ссылка</a> "
        '<A HREF="http://test.org/path?a=1">верхний регистр</A>'
    )
    print(extract_links(html))


if __name__ == "__main__":
    main()
