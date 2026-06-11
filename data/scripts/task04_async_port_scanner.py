import asyncio
import socket
import threading


async def check_port(host: str, port: int, timeout: float = 0.5) -> bool:
    try:
        _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except (OSError, asyncio.TimeoutError):
        return False


async def scan_ports(host: str, ports: list[int], concurrency: int = 500) -> list[int]:
    semaphore = asyncio.Semaphore(concurrency)
    open_ports: list[int] = []

    async def worker(port: int) -> None:
        async with semaphore:
            if await check_port(host, port):
                open_ports.append(port)

    await asyncio.gather(*(worker(port) for port in ports))
    return sorted(open_ports)


def _start_demo_listener() -> int:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen()
    port = server.getsockname()[1]

    def accept_loop() -> None:
        server.settimeout(0.5)
        while True:
            try:
                connection, _ = server.accept()
                connection.close()
            except socket.timeout:
                continue
            except OSError:
                break

    threading.Thread(target=accept_loop, daemon=True).start()
    return port


async def main() -> None:
    host = "127.0.0.1"
    demo_port = _start_demo_listener()
    ports = list(range(1, 1025)) + [demo_port]
    open_ports = await scan_ports(host, ports)
    print(f"Открытые порты на {host}: {open_ports}")
    print(f"(демо-слушатель работал на порту {demo_port})")


if __name__ == "__main__":
    asyncio.run(main())
