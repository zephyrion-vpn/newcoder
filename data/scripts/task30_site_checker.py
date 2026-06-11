import requests


def check_sites(urls: list[str], timeout: float = 5.0) -> dict[str, tuple[bool, object]]:
    report: dict[str, tuple[bool, object]] = {}
    for url in urls:
        try:
            response = requests.head(url, timeout=timeout, allow_redirects=True)
            report[url] = (response.status_code == 200, response.status_code)
        except requests.RequestException as error:
            report[url] = (False, type(error).__name__)
    return report


def main() -> None:
    sites = [
        "https://example.com",
        "https://httpbin.org/status/200",
        "https://this-domain-does-not-exist.invalid",
    ]
    for url, (ok, info) in check_sites(sites).items():
        status = "OK  " if ok else "FAIL"
        print(f"{status} {url} ({info})")


if __name__ == "__main__":
    main()
