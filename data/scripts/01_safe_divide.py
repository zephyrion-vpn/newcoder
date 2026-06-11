from typing import Optional


def safe_divide(a: object, b: object) -> Optional[float]:
    try:
        return a / b  # type: ignore[operator]
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
        return None
    except TypeError:
        print("Ошибка: оба аргумента должны быть числами.")
        return None


def main() -> None:
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide("10", 2))


if __name__ == "__main__":
    main()
