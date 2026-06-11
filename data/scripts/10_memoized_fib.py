_cache: dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть неотрицательным.")
    if n in _cache:
        return _cache[n]
    result = fib(n - 1) + fib(n - 2)
    _cache[n] = result
    return result


def main() -> None:
    print([fib(i) for i in range(15)])
    print(fib(50))


if __name__ == "__main__":
    main()
