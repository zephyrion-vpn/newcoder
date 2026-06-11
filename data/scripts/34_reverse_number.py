def reverse_number(number: int) -> int:
    return int(str(number)[::-1])


def main() -> None:
    print(reverse_number(123))


if __name__ == "__main__":
    main()
