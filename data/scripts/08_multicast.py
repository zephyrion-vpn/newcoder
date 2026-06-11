import socket
import struct
import threading
import time

MCAST_GRP = "224.1.1.1"
MCAST_PORT = 5007


def listener(received: list[str], count: int, ready: threading.Event) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    sock.settimeout(5.0)
    ready.set()
    try:
        for _ in range(count):
            data, _ = sock.recvfrom(1024)
            received.append(data.decode("utf-8"))
    except socket.timeout:
        pass
    finally:
        sock.close()


def sender(messages: list[str]) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    for message in messages:
        sock.sendto(message.encode("utf-8"), (MCAST_GRP, MCAST_PORT))
        time.sleep(0.05)
    sock.close()


def main() -> None:
    messages = [f"Сообщение #{i}" for i in range(5)]
    received: list[str] = []
    ready = threading.Event()

    listener_thread = threading.Thread(target=listener, args=(received, len(messages), ready), daemon=True)
    listener_thread.start()
    ready.wait()
    time.sleep(0.2)

    try:
        sender(messages)
    except OSError as error:
        print(f"Multicast недоступен в этой среде: {error}")
        return

    listener_thread.join(timeout=6)
    print(f"Отправлено: {len(messages)}, получено: {len(received)}")
    for message in received:
        print(f"   {message}")


if __name__ == "__main__":
    main()
