import asyncio
import random


async def producer(queue: asyncio.Queue, count: int) -> None:
    for i in range(count):
        await asyncio.sleep(random.uniform(0.001, 0.005))
        await queue.put(i)
    await queue.put(None)  # сигнал завершения не используется напрямую (см. join)


async def consumer(name: str, queue: asyncio.Queue, processed: list[int]) -> None:
    while True:
        item = await queue.get()
        try:
            if item is None:
                return
            await asyncio.sleep(random.uniform(0.001, 0.005))
            processed.append(item * item)
        finally:
            queue.task_done()


async def main() -> None:
    queue: asyncio.Queue = asyncio.Queue(maxsize=10)
    processed: list[int] = []
    total = 30
    num_consumers = 4

    consumers = [
        asyncio.create_task(consumer(f"C{i}", queue, processed))
        for i in range(num_consumers)
    ]

    for i in range(total):
        await queue.put(i)
    await queue.join()

    for _ in consumers:
        await queue.put(None)
    await asyncio.gather(*consumers)

    print(f"Сгенерировано: {total}, обработано: {len(processed)}")
    print(f"Сумма квадратов: {sum(processed)} (ожидалось {sum(i * i for i in range(total))})")


if __name__ == "__main__":
    asyncio.run(main())
