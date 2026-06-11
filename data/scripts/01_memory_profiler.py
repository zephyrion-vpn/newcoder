import functools
import tracemalloc
from typing import Callable, TypeVar

T = TypeVar("T")


def profile_memory(func: Callable[..., T]) -> Callable[..., T]:
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> T:
        already_tracing = tracemalloc.is_tracing()
        if not already_tracing:
            tracemalloc.start()
        start_current, start_peak = tracemalloc.get_traced_memory()
        try:
            result = func(*args, **kwargs)
        finally:
            current, peak = tracemalloc.get_traced_memory()
            if not already_tracing:
                tracemalloc.stop()
            delta = (peak - start_peak) / 1024
            print(f"[память] {func.__name__}: пик {peak / 1024:.1f} КБ, прирост пика {delta:.1f} КБ")
        return result

    return wrapper


@profile_memory
def build_list(n: int) -> int:
    data = [i * i for i in range(n)]
    return sum(data)


@profile_memory
def build_string(n: int) -> int:
    text = "x" * n
    return len(text)


def main() -> None:
    print("Сумма квадратов:", build_list(1_000_000))
    print("Длина строки:", build_string(5_000_000))


if __name__ == "__main__":
    main()
