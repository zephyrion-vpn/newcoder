from typing import Any, Iterator


def deep_flatten(data: Any) -> Iterator[Any]:
    if isinstance(data, (str, bytes)):
        yield data
        return
    try:
        iterator = iter(data)
    except TypeError:
        yield data
        return
    for item in iterator:
        yield from deep_flatten(item)


def main() -> None:
    print(list(deep_flatten([1, [2, [3, [4, 5]], 6], 7])))
    print(list(deep_flatten([1, ["ab", [2, 3]], (4, {5, 6})])))
    print(list(deep_flatten(42)))


if __name__ == "__main__":
    main()
