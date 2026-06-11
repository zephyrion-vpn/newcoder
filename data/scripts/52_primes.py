def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number < 4:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main() -> None:
    primes = [number for number in range(1, 101) if is_prime(number)]
    print(primes)


if __name__ == "__main__":
    main()
