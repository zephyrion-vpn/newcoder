import requests
from bs4 import BeautifulSoup


def parse_headings(html: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    return [(tag.name, tag.get_text(strip=True)) for tag in soup.find_all(["h1", "h2"])]


def fetch_headings(url: str, timeout: float = 10.0) -> list[tuple[str, str]]:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return parse_headings(response.text)


def main() -> None:
    sample = (
        "<html><body>"
        "<h1>Главный заголовок</h1>"
        "<p>текст</p>"
        "<h2>Подраздел 1</h2>"
        "<h2>Подраздел 2</h2>"
        "<h3>Не считается</h3>"
        "</body></html>"
    )
    print("[демо на локальном HTML; для сети вызовите fetch_headings(url)]")
    for level, text in parse_headings(sample):
        print(f"{level}: {text}")


if __name__ == "__main__":
    main()
