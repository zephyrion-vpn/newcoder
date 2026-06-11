import asyncio


class AsyncDBConnection:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn
        self.connected = False

    async def __aenter__(self) -> "AsyncDBConnection":
        await asyncio.sleep(0.01)  # имитация рукопожатия
        self.connected = True
        print(f"Подключение к {self.dsn} установлено.")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        await asyncio.sleep(0.01)
        self.connected = False
        print("Подключение закрыто.")
        if exc_type is not None:
            print(f"(при выходе перехвачено исключение: {exc_type.__name__})")
        return False  # не подавляем исключения

    async def query(self, sql: str) -> str:
        if not self.connected:
            raise RuntimeError("Нет подключения.")
        await asyncio.sleep(0.01)
        return f"Результат для: {sql}"


async def main() -> None:
    async with AsyncDBConnection("postgres://localhost/test") as db:
        print(await db.query("SELECT 1"))
    print(f"Состояние после выхода: connected={db.connected}")


if __name__ == "__main__":
    asyncio.run(main())
