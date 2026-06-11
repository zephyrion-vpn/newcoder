import hashlib
import os
import socket
import struct
import tempfile
import threading

CHUNK = 65536


def _sha256_of(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def server(path: str, ready: threading.Event, port_holder: list[int]) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))
    sock.listen(1)
    port_holder.append(sock.getsockname()[1])
    ready.set()
    conn, _ = sock.accept()
    with conn:
        size = os.path.getsize(path)
        checksum = _sha256_of(path).encode("ascii")
        # Заголовок: 8 байт размер + 64 байта hex-суммы.
        conn.sendall(struct.pack("!Q", size) + checksum)
        with open(path, "rb") as handle:
            for block in iter(lambda: handle.read(CHUNK), b""):
                conn.sendall(block)
    sock.close()


def client(port: int, out_path: str) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", port))
    with sock:
        header = _recv_exact(sock, 8 + 64)
        size = struct.unpack("!Q", header[:8])[0]
        expected = header[8:].decode("ascii")
        received = 0
        digest = hashlib.sha256()
        with open(out_path, "wb") as handle:
            while received < size:
                block = sock.recv(min(CHUNK, size - received))
                if not block:
                    break
                handle.write(block)
                digest.update(block)
                received += len(block)
    actual = digest.hexdigest()
    return actual == expected and received == size


def _recv_exact(sock: socket.socket, count: int) -> bytes:
    buffer = bytearray()
    while len(buffer) < count:
        block = sock.recv(count - len(buffer))
        if not block:
            raise ConnectionError("Соединение закрыто раньше времени.")
        buffer.extend(block)
    return bytes(buffer)


def main() -> None:
    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "big.bin")
    dst = os.path.join(tmp, "received.bin")
    with open(src, "wb") as handle:
        handle.write(os.urandom(5 * 1024 * 1024))  # 5 МБ

    ready = threading.Event()
    port_holder: list[int] = []
    server_thread = threading.Thread(target=server, args=(src, ready, port_holder), daemon=True)
    server_thread.start()
    ready.wait()

    ok = client(port_holder[0], dst)
    server_thread.join(timeout=10)

    print(f"Передано байт: {os.path.getsize(dst)}")
    print(f"SHA256 совпадает: {ok}")
    print(f"MD5 исходного == MD5 полученного: {_md5(src) == _md5(dst)}")


def _md5(path: str) -> str:
    digest = hashlib.md5()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


if __name__ == "__main__":
    main()
