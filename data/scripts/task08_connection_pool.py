import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator


class Connection:
    def __init__(self, connection_id: int) -> None:
        self.connection_id = connection_id

    async def execute(self, query: str) -> str:
        await asyncio.sleep(0.1)
        return f"[conn {self.connection_id}] {query}"


class ConnectionPool:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Размер пула должен быть положительным.")
        self._free = [Connection(i) for i in range(size)]
        self._condition = asyncio.Condition()

    async def acquire(self) -> Connection:
        async with self._condition:
            while not self._free:
                await self._condition.wait()
            return self._free.pop()

    async def release(self, connection: Connection) -> None:
        async with self._condition:
            self._free.append(connection)
            self._condition.notify()

    @asynccontextmanager
    async def connection(self) -> AsyncIterator[Connection]:
        acquired = await self.acquire()
        try:
            yield acquired
        finally:
            await self.release(acquired)


async def main() -> None:
    pool = ConnectionPool(size=2)

    async def task(task_id: int) -> None:
        async with pool.connection() as connection:
            result = await connection.execute(f"SELECT {task_id}")
            print(result)

    await asyncio.gather(*(task(i) for i in range(6)))


if __name__ == "__main__":
    asyncio.run(main())
