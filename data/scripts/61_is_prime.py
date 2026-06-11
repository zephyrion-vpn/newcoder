def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def main() -> None:
    for number in (1, 2, 7, 10, 13, 100, 101):
        print(f"{number}: {is_prime(number)}")


if __name__ == "__main__":
    main()
