def read_non_negative_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Введите целое число.")
            continue
        if value < 0:
            print("Значение не может быть отрицательным.")
            continue
        return value


def to_seconds(hours: int, minutes: int, seconds: int) -> int:
    return hours * 3600 + minutes * 60 + seconds


def main() -> None:
    hours = read_non_negative_int("Введите количество часов: ")
    minutes = read_non_negative_int("Введите количество минут: ")
    seconds = read_non_negative_int("Введите количество секунд: ")
    print(f"Всего секунд: {to_seconds(hours, minutes, seconds)}")


if __name__ == "__main__":
    main()
