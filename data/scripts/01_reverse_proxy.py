import http.server
import socketserver
import threading
import urllib.request
import urllib.error


def make_backend(name: str) -> type[http.server.BaseHTTPRequestHandler]:
    class BackendHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            body = f"Ответ от {name}, путь {self.path}".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args: object) -> None:
            pass

    return BackendHandler


class ReverseProxyHandler(http.server.BaseHTTPRequestHandler):
    backends: list[str] = []
    _index = 0
    _lock = threading.Lock()

    @classmethod
    def next_backend(cls) -> str:
        with cls._lock:
            backend = cls.backends[cls._index % len(cls.backends)]
            cls._index += 1
        return backend

    def do_GET(self) -> None:
        backend = self.next_backend()
        try:
            with urllib.request.urlopen(f"{backend}{self.path}", timeout=5) as response:
                data = response.read()
                code = response.status
        except urllib.error.URLError as error:
            self.send_error(502, f"Bad Gateway: {error}")
            return
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("X-Proxied-To", backend)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args: object) -> None:
        pass


def _serve(handler: type[http.server.BaseHTTPRequestHandler]) -> tuple[socketserver.TCPServer, int]:
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, port


def main() -> None:
    backend_servers = []
    backend_urls = []
    for name in ("backend-1", "backend-2"):
        server, port = _serve(make_backend(name))
        backend_servers.append(server)
        backend_urls.append(f"http://127.0.0.1:{port}")

    ReverseProxyHandler.backends = backend_urls
    proxy, proxy_port = _serve(ReverseProxyHandler)

    for i in range(4):
        with urllib.request.urlopen(f"http://127.0.0.1:{proxy_port}/req{i}") as response:
            print(f"Запрос {i}: {response.read().decode('utf-8')}")

    proxy.shutdown()
    for server in backend_servers:
        server.shutdown()
    print("Прокси и бэкенды остановлены.")


if __name__ == "__main__":
    main()
