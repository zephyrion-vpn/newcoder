def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def main() -> None:
    print(is_prime(13))


if __name__ == "__main__":
    main()
