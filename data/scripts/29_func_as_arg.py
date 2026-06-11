from typing import Callable


def apply(func: Callable[[str], str], value: str) -> str:
    return func(value)


if __name__ == "__main__":
    print(apply(str.upper, "hi"))
