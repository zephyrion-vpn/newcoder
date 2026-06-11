def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(number))


def main() -> None:
    print(digit_sum(1234))


if __name__ == "__main__":
    main()
