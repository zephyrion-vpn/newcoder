import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PAGE = (
    "<!DOCTYPE html><html lang='ru'><head><meta charset='utf-8'>"
    "<title>Демо</title></head>"
    "<body><h1>Привет от http.server</h1></body></html>"
).encode("utf-8")


class StaticHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(PAGE)))
        self.end_headers()
        self.wfile.write(PAGE)

    def log_message(self, *args: object) -> None:
        pass


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), StaticHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/") as response:
            print("Статус:", response.status)
            print("Тело:", response.read().decode("utf-8"))
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
