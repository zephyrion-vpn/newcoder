import asyncio
import random
from typing import AsyncGenerator


async def websocket_stream(stop: asyncio.Event | None = None) -> AsyncGenerator[str, None]:
    frame = 0
    while stop is None or not stop.is_set():
        await asyncio.sleep(random.uniform(0.05, 0.2))
        frame += 1
        yield f"frame-{frame}"


async def consume(limit: int) -> list[str]:
    received: list[str] = []
    async for message in websocket_stream():
        received.append(message)
        print("получено:", message)
        if len(received) >= limit:
            break
    return received


async def main() -> None:
    messages = await consume(limit=5)
    print("Всего получено:", len(messages))


if __name__ == "__main__":
    asyncio.run(main())
