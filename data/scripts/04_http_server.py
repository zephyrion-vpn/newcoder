import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

HTML_PAGE = """<!DOCTYPE html>
<html lang="ru">
<head><meta charset="utf-8"><title>Демо-сервер</title></head>
<body><h1>Привет от http.server!</h1><p>Статическая страница.</p></body>
</html>"""


class StaticHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        body = HTML_PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args: object) -> None:
        pass


def run_server(host: str = "127.0.0.1", port: int = 8000) -> HTTPServer:
    return HTTPServer((host, port), StaticHandler)


def main() -> None:
    server = run_server(port=0)
    host, port = server.server_address
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    try:
        url = "http://" + host + ":" + str(port) + "/"
        with urllib.request.urlopen(url, timeout=5) as response:
            print(f"Статус: {response.status}")
            print("Первая строка тела:", response.read().decode("utf-8").splitlines()[0])
    finally:
        server.shutdown()
        thread.join()
        server.server_close()
    print("Сервер остановлен.")


if __name__ == "__main__":
    main()
