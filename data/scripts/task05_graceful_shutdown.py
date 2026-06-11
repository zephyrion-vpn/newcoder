import asyncio
import os
import signal
import threading
import time


class Application:
    def __init__(self) -> None:
        self._tasks: set[asyncio.Task] = set()
        self._connections: list[str] = []
        self._stop = asyncio.Event()

    async def _worker(self, name: str) -> None:
        try:
            while not self._stop.is_set():
                await asyncio.sleep(0.3)
                print(f"{name} работает")
        except asyncio.CancelledError:
            print(f"{name} отменён")
            raise

    async def _close_connections(self) -> None:
        for connection in self._connections:
            await asyncio.sleep(0.05)
            print(f"Закрыто соединение: {connection}")
        self._connections.clear()

    def _request_shutdown(self) -> None:
        self._stop.set()

    def _install_signal_handlers(self, loop: asyncio.AbstractEventLoop) -> None:
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self._request_shutdown)
            except NotImplementedError:
                signal.signal(sig, lambda *_: loop.call_soon_threadsafe(self._request_shutdown))

    async def run(self) -> None:
        self._install_signal_handlers(asyncio.get_running_loop())
        self._connections = ["база данных", "кэш"]
        for i in range(3):
            self._tasks.add(asyncio.create_task(self._worker(f"worker-{i}")))

        await self._stop.wait()
        print("\nПолучен сигнал завершения, останавливаемся…")
        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        await self._close_connections()
        print("Graceful shutdown завершён.")


def _demo_interrupt(delay: float) -> None:
    def fire() -> None:
        time.sleep(delay)
        os.kill(os.getpid(), signal.SIGINT)

    threading.Thread(target=fire, daemon=True).start()


def main() -> None:
    _demo_interrupt(1.5)
    asyncio.run(Application().run())


if __name__ == "__main__":
    main()
