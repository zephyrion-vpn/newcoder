import random

LOWER, UPPER = 1, 100


def read_guess(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def main() -> None:
    secret = random.randint(LOWER, UPPER)
    attempts = 0
    print(f"Я загадал число от {LOWER} до {UPPER}.")
    while True:
        guess = read_guess("Ваша догадка: ")
        attempts += 1
        if guess < secret:
            print("Больше.")
        elif guess > secret:
            print("Меньше.")
        else:
            print(f"Верно! Попыток: {attempts}.")
            return


if __name__ == "__main__":
    main()
