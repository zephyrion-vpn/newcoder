import asyncio
import functools
import random
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")


def retry_with_backoff(
    retries: int = 3,
    base_delay: float = 0.1,
    factor: float = 2.0,
    max_delay: float = 10.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
    jitter: bool = True,
) -> Callable[[Callable[..., Awaitable[T]]], Callable[..., Awaitable[T]]]:
    if retries < 1:
        raise ValueError("retries должно быть не меньше 1.")

    def decorator(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args: object, **kwargs: object) -> T:
            delay = base_delay
            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as error:
                    if attempt == retries:
                        raise
                    sleep_for = min(delay, max_delay)
                    if jitter:
                        sleep_for = random.uniform(0, sleep_for)
                    print(f"Попытка {attempt} неудачна ({error}), повтор через {sleep_for:.2f}s")
                    await asyncio.sleep(sleep_for)
                    delay *= factor
            raise AssertionError("unreachable")

        return wrapper

    return decorator


@retry_with_backoff(retries=5, base_delay=0.1)
async def flaky_call() -> str:
    if random.random() < 0.7:
        raise ConnectionError("сервер недоступен")
    return "успех"


async def main() -> None:
    random.seed(1)
    result = await flaky_call()
    print("Результат:", result)


if __name__ == "__main__":
    asyncio.run(main())
