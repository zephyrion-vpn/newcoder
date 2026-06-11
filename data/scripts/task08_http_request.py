import socket
import urllib.error
import urllib.request


def fetch(url: str, timeout: float = 5.0) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except (socket.timeout, TimeoutError):
        print(f"Таймаут при запросе к {url}")
        return None
    except urllib.error.URLError as error:
        reason = getattr(error, "reason", error)
        if isinstance(reason, (socket.timeout, TimeoutError)):
            print(f"Таймаут соединения с {url}")
        else:
            print(f"Ошибка соединения с {url}: {reason}")
        return None
    except ConnectionError as error:
        print(f"Ошибка соединения с {url}: {error}")
        return None
    except OSError as error:
        print(f"Сетевая ошибка при запросе к {url}: {error}")
        return None


def main() -> None:
    body = fetch("http://10.255.255.1", timeout=2.0)
    if body is None:
        print("Запрос не выполнен (ожидаемо без доступа к сети)")
    else:
        print("Получено байт:", len(body))


if __name__ == "__main__":
    main()
