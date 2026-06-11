from typing import Any


def call_if_callable(obj: Any) -> Any:
    if callable(obj):
        return obj(42)
    return f"Объект {obj!r} не является вызываемым."


def main() -> None:
    print(call_if_callable(lambda x: x + 1))
    print(call_if_callable(str))
    print(call_if_callable(100))
    print(call_if_callable("не функция"))


if __name__ == "__main__":
    main()
