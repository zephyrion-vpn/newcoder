import socket
import threading
import time
from urllib.parse import urlparse


class HttpResponse:
    def __init__(self, status: int, headers: dict[str, str], body: bytes) -> None:
        self.status = status
        self.headers = headers
        self.body = body


def _parse_response(raw: bytes) -> HttpResponse:
    head, _, body = raw.partition(b"\r\n\r\n")
    lines = head.decode("latin-1").split("\r\n")
    status = int(lines[0].split(" ")[1])
    headers = {}
    for line in lines[1:]:
        if ": " in line:
            name, value = line.split(": ", 1)
            headers[name.lower()] = value
    return HttpResponse(status, headers, body)


def http_get(url: str, retries: int = 3, timeout: float = 5.0, backoff: float = 0.5) -> HttpResponse:
    parsed = urlparse(url)
    if parsed.scheme != "http":
        raise ValueError("Поддерживается только http")
    host = parsed.hostname or ""
    port = parsed.port or 80
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    request = (
        f"GET {path} HTTP/1.1\r\nHost: {host}\r\n"
        "User-Agent: custom-client/1.0\r\nConnection: close\r\n\r\n"
    )
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with socket.create_connection((host, port), timeout) as sock:
                sock.settimeout(timeout)
                sock.sendall(request.encode("latin-1"))
                chunks: list[bytes] = []
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
            return _parse_response(b"".join(chunks))
        except (OSError, socket.timeout) as error:
            last_error = error
            print(f"Попытка {attempt} неудачна: {error}")
            if attempt < retries:
                time.sleep(backoff * attempt)
    raise ConnectionError(f"Не удалось после {retries} попыток: {last_error}")


def _start_demo_server() -> tuple[int, threading.Event]:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen()
    port = server.getsockname()[1]
    stop = threading.Event()

    def serve() -> None:
        server.settimeout(0.5)
        while not stop.is_set():
            try:
                connection, _ = server.accept()
            except socket.timeout:
                continue
            with connection:
                connection.recv(1024)
                body = "Привет от демо-сервера".encode()
                connection.sendall(
                    b"HTTP/1.1 200 OK\r\nContent-Length: "
                    + str(len(body)).encode()
                    + b"\r\nConnection: close\r\n\r\n"
                    + body
                )
        server.close()

    threading.Thread(target=serve, daemon=True).start()
    return port, stop


def main() -> None:
    port, stop = _start_demo_server()
    try:
        response = http_get(f"http://127.0.0.1:{port}/")
        print("Статус:", response.status)
        print("Тело:", response.body.decode())
    finally:
        stop.set()


if __name__ == "__main__":
    main()
