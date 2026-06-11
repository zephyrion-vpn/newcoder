import socket
import statistics
import threading
import time


def echo_server(ready: threading.Event, port_holder: list[int], stop: threading.Event) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))
    sock.settimeout(0.5)
    port_holder.append(sock.getsockname()[1])
    ready.set()
    while not stop.is_set():
        try:
            data, addr = sock.recvfrom(1024)
            sock.sendto(data, addr)
        except socket.timeout:
            continue
    sock.close()


def measure(port: int, samples: int = 30) -> dict[str, float]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    latencies: list[float] = []
    for i in range(samples):
        payload = str(i).encode()
        start = time.perf_counter()
        sock.sendto(payload, ("127.0.0.1", port))
        try:
            sock.recvfrom(1024)
        except socket.timeout:
            continue
        latencies.append((time.perf_counter() - start) * 1000)
        time.sleep(0.005)
    sock.close()

    if not latencies:
        return {}
    jitter = statistics.mean(abs(latencies[i] - latencies[i - 1]) for i in range(1, len(latencies))) if len(latencies) > 1 else 0.0
    return {
        "samples": len(latencies),
        "min": min(latencies),
        "max": max(latencies),
        "avg": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "jitter": jitter,
    }


def main() -> None:
    ready = threading.Event()
    stop = threading.Event()
    port_holder: list[int] = []
    server_thread = threading.Thread(target=echo_server, args=(ready, port_holder, stop), daemon=True)
    server_thread.start()
    ready.wait()

    stats = measure(port_holder[0])
    stop.set()
    server_thread.join(timeout=2)

    if not stats:
        print("Не удалось измерить (нет ответов).")
        return
    print(f"Выборок: {stats['samples']}")
    print(f"Мин/Средн/Макс: {stats['min']:.3f} / {stats['avg']:.3f} / {stats['max']:.3f} мс")
    print(f"Медиана: {stats['median']:.3f} мс")
    print(f"Джиттер: {stats['jitter']:.3f} мс")


if __name__ == "__main__":
    main()
