import socket
import threading
from pathlib import Path


class HttpServer:
    def __init__(self, root: Path, host: str = "127.0.0.1", port: int = 0) -> None:
        self._root = root
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((host, port))
        self._server.listen()
        self._running = False

    @property
    def address(self) -> tuple[str, int]:
        return self._server.getsockname()

    def _parse_request(self, raw: bytes) -> tuple[str, str, dict[str, str]]:
        text = raw.decode("latin-1")
        head = text.split("\r\n\r\n", 1)[0]
        lines = head.split("\r\n")
        method, path, _ = lines[0].split(" ")
        headers = {}
        for line in lines[1:]:
            if ": " in line:
                name, value = line.split(": ", 1)
                headers[name.lower()] = value
        return method, path, headers

    def _build_response(self, method: str, path: str) -> bytes:
        if method != "GET":
            return self._response(405, "text/plain", b"Method Not Allowed")
        target = self._root / (path.lstrip("/") or "index.html")
        if not target.is_file() or self._root not in target.resolve().parents and target.resolve() != (self._root / target.name).resolve():
            target = self._root / path.lstrip("/")
        if target.is_file():
            return self._response(200, "text/html; charset=utf-8", target.read_bytes())
        return self._response(404, "text/plain; charset=utf-8", "Не найдено".encode())

    def _response(self, status: int, content_type: str, body: bytes) -> bytes:
        reasons = {200: "OK", 404: "Not Found", 405: "Method Not Allowed"}
        head = (
            f"HTTP/1.1 {status} {reasons[status]}\r\n"
            f"Content-Type: {content_type}\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n\r\n"
        )
        return head.encode("latin-1") + body

    def _handle(self, connection: socket.socket) -> None:
        with connection:
            raw = b""
            while b"\r\n\r\n" not in raw:
                chunk = connection.recv(1024)
                if not chunk:
                    return
                raw += chunk
            method, path, _ = self._parse_request(raw)
            connection.sendall(self._build_response(method, path))

    def serve_forever(self) -> None:
        self._running = True
        self._server.settimeout(0.5)
        while self._running:
            try:
                connection, _ = self._server.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            threading.Thread(target=self._handle, args=(connection,), daemon=True).start()

    def stop(self) -> None:
        self._running = False
        self._server.close()


def main() -> None:
    import tempfile

    root = Path(tempfile.mkdtemp())
    (root / "index.html").write_text("<h1>Привет от HTTP-сервера</h1>", encoding="utf-8")
    server = HttpServer(root)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.address
        with socket.create_connection((host, port), timeout=2) as sock:
            sock.sendall(f"GET /index.html HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
            response = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk
        print(response.decode("utf-8"))
    finally:
        server.stop()
        thread.join()


if __name__ == "__main__":
    main()
