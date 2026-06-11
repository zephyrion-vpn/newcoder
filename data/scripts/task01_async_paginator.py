import asyncio
from typing import Any, Awaitable, Callable

Page = tuple[list[Any], Any | None]
FetchPage = Callable[[Any | None], Awaitable[Page]]


class AsyncPaginator:
    def __init__(self, fetch_page: FetchPage, start_cursor: Any | None = None) -> None:
        self._fetch_page = fetch_page
        self._cursor = start_cursor
        self._buffer: list[Any] = []
        self._index = 0
        self._exhausted = False

    def __aiter__(self) -> "AsyncPaginator":
        return self

    async def __anext__(self) -> Any:
        while self._index >= len(self._buffer):
            if self._exhausted:
                raise StopAsyncIteration
            self._buffer, self._cursor = await self._fetch_page(self._cursor)
            self._index = 0
            if self._cursor is None:
                self._exhausted = True
        item = self._buffer[self._index]
        self._index += 1
        return item


def make_mock_api(pages: list[list[Any]]) -> FetchPage:
    async def fetch_page(cursor: int | None) -> Page:
        index = cursor or 0
        await asyncio.sleep(0.05)
        print(f"  [запрос страницы {index}]")
        next_cursor = index + 1 if index + 1 < len(pages) else None
        return pages[index], next_cursor

    return fetch_page


async def main() -> None:
    pages = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    async for item in AsyncPaginator(make_mock_api(pages)):
        print("получен:", item)


if __name__ == "__main__":
    asyncio.run(main())
