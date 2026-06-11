import selectors
import socket
import threading


class EchoServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 0) -> None:
        self._selector = selectors.DefaultSelector()
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((host, port))
        self._server.listen()
        self._server.setblocking(False)
        self._selector.register(self._server, selectors.EVENT_READ, self._accept)
        self._running = False

    @property
    def address(self) -> tuple[str, int]:
        return self._server.getsockname()

    def _accept(self, sock: socket.socket) -> None:
        connection, _ = sock.accept()
        connection.setblocking(False)
        self._selector.register(connection, selectors.EVENT_READ, self._read)

    def _read(self, connection: socket.socket) -> None:
        data = connection.recv(4096)
        if data:
            connection.sendall(data)
        else:
            self._selector.unregister(connection)
            connection.close()

    def serve_forever(self) -> None:
        self._running = True
        while self._running:
            for key, _ in self._selector.select(timeout=0.5):
                key.data(key.fileobj)

    def stop(self) -> None:
        self._running = False

    def close(self) -> None:
        self._selector.close()
        self._server.close()


def main() -> None:
    server = EchoServer()
    host, port = server.address
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with socket.create_connection((host, port), timeout=2) as client:
            client.sendall("привет, event loop".encode())
            print("Эхо:", client.recv(4096).decode())
    finally:
        server.stop()
        thread.join()
        server.close()


if __name__ == "__main__":
    main()
