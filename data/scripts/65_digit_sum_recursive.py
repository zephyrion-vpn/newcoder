def digit_sum(n: int) -> int:
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def main() -> None:
    for number in (0, 5, 123, 99999):
        print(f"{number} -> {digit_sum(number)}")


if __name__ == "__main__":
    main()
