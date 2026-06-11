import socket
import urllib.error
import urllib.request
from typing import Optional


def fetch_url(url: str, timeout: float = 5.0) -> Optional[str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        print(f"HTTP ошибка: {error.code} {error.reason}")
    except urllib.error.URLError as error:
        reason = error.reason
        if isinstance(reason, (TimeoutError, socket.timeout)):
            print("Ошибка: истекло время ожидания (timeout).")
        else:
            print(f"Ошибка соединения: {reason}")
    except (TimeoutError, socket.timeout):
        print("Ошибка: истекло время ожидания (timeout).")
    except ConnectionError as error:
        print(f"Ошибка соединения: {error}")
    except OSError as error:
        print(f"Сетевая ошибка: {error}")
    return None


def main() -> None:
    result = fetch_url("http://10.255.255.1", timeout=1.0)
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
