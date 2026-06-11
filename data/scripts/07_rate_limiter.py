import asyncio
import time


class TokenBucket:
    def __init__(self, rate: float, capacity: float | None = None) -> None:
        self.rate = rate
        self.capacity = capacity if capacity is not None else rate
        self.tokens = self.capacity
        self.updated = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self, amount: float = 1.0) -> None:
        async with self._lock:
            while True:
                now = time.monotonic()
                elapsed = now - self.updated
                self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
                self.updated = now
                if self.tokens >= amount:
                    self.tokens -= amount
                    return
                deficit = amount - self.tokens
                await asyncio.sleep(deficit / self.rate)


async def main() -> None:
    limiter = TokenBucket(rate=5, capacity=5)  # 5 вызовов/сек
    timestamps: list[float] = []
    start = time.monotonic()

    async def call(i: int) -> None:
        await limiter.acquire()
        timestamps.append(time.monotonic() - start)

    await asyncio.gather(*(call(i) for i in range(15)))
    print(f"Выполнено вызовов: {len(timestamps)}")
    print(f"Общее время: {timestamps[-1]:.2f} с (ожидаем ≈ 2 с для 15 вызовов при 5/с)")


if __name__ == "__main__":
    asyncio.run(main())
