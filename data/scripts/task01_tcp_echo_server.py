import socket
import threading


class ThreadedEchoServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 0) -> None:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((host, port))
        self._server.listen()
        self._running = False

    @property
    def address(self) -> tuple[str, int]:
        return self._server.getsockname()

    def _handle(self, connection: socket.socket) -> None:
        with connection:
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                connection.sendall(data)

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


def _client(address: tuple[str, int], message: str) -> str:
    with socket.create_connection(address, timeout=2) as sock:
        sock.sendall(message.encode())
        return sock.recv(4096).decode()


def main() -> None:
    server = ThreadedEchoServer()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        results = [_client(server.address, f"клиент {i}") for i in range(3)]
        for echo in results:
            print("Эхо:", echo)
    finally:
        server.stop()
        thread.join()


if __name__ == "__main__":
    main()
