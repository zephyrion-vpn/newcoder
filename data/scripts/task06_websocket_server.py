import base64
import hashlib
import socket
import struct
import threading

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def accept_key(key: str) -> str:
    digest = hashlib.sha1((key + GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode("ascii")


def handshake(connection: socket.socket) -> None:
    request = b""
    while b"\r\n\r\n" not in request:
        chunk = connection.recv(1024)
        if not chunk:
            return
        request += chunk
    headers: dict[str, str] = {}
    for line in request.decode("latin-1").split("\r\n")[1:]:
        if ": " in line:
            name, value = line.split(": ", 1)
            headers[name.lower()] = value
    response = (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Accept: {accept_key(headers['sec-websocket-key'])}\r\n\r\n"
    )
    connection.sendall(response.encode("latin-1"))


def read_frame(connection: socket.socket) -> tuple[int, bytes] | None:
    header = connection.recv(2)
    if len(header) < 2:
        return None
    opcode = header[0] & 0x0F
    masked = header[1] & 0x80
    length = header[1] & 0x7F
    if length == 126:
        length = struct.unpack(">H", connection.recv(2))[0]
    elif length == 127:
        length = struct.unpack(">Q", connection.recv(8))[0]
    mask = connection.recv(4) if masked else b""
    payload = bytearray(connection.recv(length))
    if masked:
        for i in range(len(payload)):
            payload[i] ^= mask[i % 4]
    return opcode, bytes(payload)


def send_frame(connection: socket.socket, payload: bytes, opcode: int = 0x1) -> None:
    header = struct.pack("B", 0x80 | opcode)
    length = len(payload)
    if length < 126:
        header += struct.pack("B", length)
    elif length < 65536:
        header += struct.pack("B", 126) + struct.pack(">H", length)
    else:
        header += struct.pack("B", 127) + struct.pack(">Q", length)
    connection.sendall(header + payload)


class WebSocketServer:
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
            handshake(connection)
            while True:
                frame = read_frame(connection)
                if frame is None:
                    break
                opcode, payload = frame
                if opcode == 0x8:
                    break
                if opcode == 0x1:
                    send_frame(connection, payload)

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


def _demo_client(address: tuple[str, int], message: str) -> str:
    key = base64.b64encode(b"0123456789abcdef").decode("ascii")
    with socket.create_connection(address, timeout=2) as sock:
        request = (
            f"GET / HTTP/1.1\r\nHost: {address[0]}:{address[1]}\r\n"
            "Upgrade: websocket\r\nConnection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n"
        )
        sock.sendall(request.encode("latin-1"))
        response = b""
        while b"\r\n\r\n" not in response:
            response += sock.recv(1024)
        payload = message.encode()
        mask = b"\x12\x34\x56\x78"
        masked = bytes(byte ^ mask[i % 4] for i, byte in enumerate(payload))
        frame = struct.pack("BB", 0x81, 0x80 | len(payload)) + mask + masked
        sock.sendall(frame)
        header = sock.recv(2)
        length = header[1] & 0x7F
        return sock.recv(length).decode()


def main() -> None:
    server = WebSocketServer()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        echo = _demo_client(server.address, "привет, WebSocket")
        print("Эхо от бота:", echo)
    finally:
        server.stop()
        thread.join()


if __name__ == "__main__":
    main()
