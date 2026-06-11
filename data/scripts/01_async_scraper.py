import asyncio
import random
from typing import Awaitable, Callable

try:
    import aiohttp  # type: ignore
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False


async def _aiohttp_fetch(session: "aiohttp.ClientSession", url: str) -> int:
    async with session.get(url) as response:
        await response.text()
        return response.status


async def scrape(
    urls: list[str],
    concurrency: int = 10,
    fetcher: Callable[[str], Awaitable[int]] | None = None,
) -> dict[str, int]:
    semaphore = asyncio.Semaphore(concurrency)
    results: dict[str, int] = {}

    async def worker(url: str, fetch: Callable[[str], Awaitable[int]]) -> None:
        async with semaphore:
            results[url] = await fetch(url)

    if fetcher is not None:
        await asyncio.gather(*(worker(url, fetcher) for url in urls))
        return results

    if HAS_AIOHTTP:
        async with aiohttp.ClientSession() as session:
            async def real_fetch(url: str) -> int:
                return await _aiohttp_fetch(session, url)
            await asyncio.gather(*(worker(url, real_fetch) for url in urls))
        return results

    raise RuntimeError("aiohttp не установлен и не передан резервный fetcher.")


async def main() -> None:
    urls = ["https://example.com/page/" + str(i) for i in range(100)]
    active = 0
    peak = 0
    lock = asyncio.Lock()

    async def mock_fetch(url: str) -> int:
        nonlocal active, peak
        async with lock:
            active += 1
            peak = max(peak, active)
        await asyncio.sleep(random.uniform(0.001, 0.01))
        async with lock:
            active -= 1
        return 200

    results = await scrape(urls, concurrency=10, fetcher=mock_fetch)
    print(f"aiohttp доступен: {HAS_AIOHTTP}")
    print(f"Обработано URL: {len(results)}")
    print(f"Пик одновременных запросов: {peak} (лимит 10)")
    print(f"Все успешны: {all(code == 200 for code in results.values())}")


if __name__ == "__main__":
    asyncio.run(main())
