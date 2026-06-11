from __future__ import annotations

from typing import Any, Optional


class Singleton:
    _instance: Optional["Singleton"] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "Singleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: Any = None) -> None:
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True


def main() -> None:
    first = Singleton("первый")
    second = Singleton("второй")
    print(first is second)
    print(first.value)
    print(second.value)


if __name__ == "__main__":
    main()
