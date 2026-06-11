from typing import Iterator


def primes_up_to(n: int) -> Iterator[int]:
    if n < 2:
        return
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for number in range(2, n + 1):
        if sieve[number]:
            yield number
            for multiple in range(number * number, n + 1, number):
                sieve[multiple] = False


def main() -> None:
    print(list(primes_up_to(30)))
    print(list(primes_up_to(1)))


if __name__ == "__main__":
    main()
