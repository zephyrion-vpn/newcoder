def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def main() -> None:
    print(is_palindrome(121))


if __name__ == "__main__":
    main()
