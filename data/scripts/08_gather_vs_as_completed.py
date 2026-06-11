import asyncio
import time


async def task(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} (задержка {delay}с)"


async def demo_gather() -> None:
    start = time.monotonic()
    coros = [task("A", 0.3), task("B", 0.1), task("C", 0.2)]
    results = await asyncio.gather(*coros)
    print(f"gather — результаты в порядке аргументов за {time.monotonic() - start:.2f}с:")
    for r in results:
        print(f"   {r}")


async def demo_as_completed() -> None:
    start = time.monotonic()
    coros = [task("A", 0.3), task("B", 0.1), task("C", 0.2)]
    print("as_completed — результаты по мере готовности:")
    for coro in asyncio.as_completed(coros):
        result = await coro
        print(f"   {result} на {time.monotonic() - start:.2f}с")


async def main() -> None:
    await demo_gather()
    await demo_as_completed()


if __name__ == "__main__":
    asyncio.run(main())
