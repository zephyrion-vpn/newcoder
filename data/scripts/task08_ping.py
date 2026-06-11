import os
import select
import socket
import struct
import sys
import time


def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i + 1]
    total = (total >> 16) + (total & 0xFFFF)
    total += total >> 16
    return ~total & 0xFFFF


def build_packet(identifier: int, sequence: int) -> bytes:
    header = struct.pack(">BBHHH", 8, 0, 0, identifier, sequence)
    payload = struct.pack(">d", time.time())
    check = checksum(header + payload)
    header = struct.pack(">BBHHH", 8, 0, check, identifier, sequence)
    return header + payload


def ping(host: str, count: int = 4, timeout: float = 1.0) -> None:
    destination = socket.gethostbyname(host)
    identifier = os.getpid() & 0xFFFF
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
        sock.settimeout(timeout)
        for sequence in range(1, count + 1):
            sock.sendto(build_packet(identifier, sequence), (destination, 0))
            start = time.perf_counter()
            ready, _, _ = select.select([sock], [], [], timeout)
            if not ready:
                print(f"{host}: таймаут seq={sequence}")
                continue
            data, _ = sock.recvfrom(1024)
            msg_type, _, _, recv_id, recv_seq = struct.unpack(">BBHHH", data[20:28])
            if msg_type == 0 and recv_id == identifier:
                elapsed = (time.perf_counter() - start) * 1000
                print(f"{host}: ответ seq={recv_seq} time={elapsed:.2f} ms")
            time.sleep(0.2)


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    try:
        ping(host)
    except PermissionError:
        print("Для ICMP raw socket нужны права root (запустите через sudo).")
    except OSError as error:
        print(f"Ошибка сети: {error}")


if __name__ == "__main__":
    main()
