def safe_divide(a: object, b: object) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return None
    except TypeError:
        print("Ошибка: оба аргумента должны быть числами")
        return None


def main() -> None:
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))
    print('"10" / 2 =', safe_divide("10", 2))


if __name__ == "__main__":
    main()
