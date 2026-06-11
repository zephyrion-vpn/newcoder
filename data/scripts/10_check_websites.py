import urllib.error
import urllib.request


def check_website(url: str, timeout: float = 5.0) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            return status == 200, f"{status}"
    except urllib.error.HTTPError as error:
        return False, f"HTTP {error.code}"
    except urllib.error.URLError as error:
        return False, f"ошибка: {error.reason}"
    except Exception as error:  # noqa: BLE001
        return False, f"ошибка: {error}"


def check_all(urls: list[str]) -> None:
    for url in urls:
        ok, detail = check_website(url)
        mark = "✓" if ok else "✗"
        print(f"{mark} {url} — {detail}")


def main() -> None:
    urls = [
        "https://www.example.com",
        "https://httpbin.org/status/404",
        "https://nonexistent-domain-xyz-123456.org",
    ]
    check_all(urls)


if __name__ == "__main__":
    main()
