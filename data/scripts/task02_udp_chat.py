import socket
import threading
import time


class UdpChatServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 0) -> None:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((host, port))
        self._clients: set[tuple[str, int]] = set()
        self._running = False

    @property
    def address(self) -> tuple[str, int]:
        return self._sock.getsockname()

    def serve_forever(self) -> None:
        self._running = True
        self._sock.settimeout(0.5)
        while self._running:
            try:
                data, sender = self._sock.recvfrom(4096)
            except socket.timeout:
                continue
            except OSError:
                break
            self._clients.add(sender)
            for client in self._clients:
                self._sock.sendto(data, client)

    def stop(self) -> None:
        self._running = False
        self._sock.close()


def _make_client(server_address: tuple[str, int], name: str) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))
    sock.settimeout(1.0)
    sock.sendto(f"{name} подключился".encode(), server_address)
    return sock


def _drain(sock: socket.socket) -> None:
    try:
        while True:
            sock.recvfrom(4096)
    except socket.timeout:
        return


def main() -> None:
    server = UdpChatServer()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        alice = _make_client(server.address, "Алиса")
        bob = _make_client(server.address, "Боб")
        time.sleep(0.2)
        _drain(alice)
        _drain(bob)
        alice.sendto("Алиса: привет всем!".encode(), server.address)
        time.sleep(0.2)
        for name, sock in (("Алиса", alice), ("Боб", bob)):
            data, _ = sock.recvfrom(4096)
            print(f"{name} получил: {data.decode()}")
        alice.close()
        bob.close()
    finally:
        server.stop()
        thread.join()


if __name__ == "__main__":
    main()
