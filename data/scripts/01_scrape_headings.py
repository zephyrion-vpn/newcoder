from html.parser import HTMLParser
from typing import Optional

try:
    import requests  # type: ignore
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    HAS_REQUESTS = False


class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._current: Optional[str] = None
        self.headings: list[tuple[str, str]] = []
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag in ("h1", "h2"):
            self._current = tag
            self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == self._current:
            text = "".join(self._buffer).strip()
            if text:
                self.headings.append((tag, text))
            self._current = None

    def handle_data(self, data: str) -> None:
        if self._current:
            self._buffer.append(data)


def fetch_html(url: str, timeout: float = 10.0) -> str:
    if HAS_REQUESTS:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_headings(html: str) -> list[tuple[str, str]]:
    parser = HeadingParser()
    parser.feed(html)
    return parser.headings


def main() -> None:
    sample = """
    <html><body>
        <h1>Главный заголовок</h1>
        <p>текст</p>
        <h2>Подзаголовок 1</h2>
        <h2>Подзаголовок 2</h2>
    </body></html>
    """
    for tag, text in extract_headings(sample):
        print(f"<{tag}> {text}")


if __name__ == "__main__":
    main()
