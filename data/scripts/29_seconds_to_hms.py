def seconds_to_hms(total_seconds: int) -> str:
    if not isinstance(total_seconds, int) or isinstance(total_seconds, bool):
        raise TypeError("ожидается целое число секунд")
    if total_seconds < 0:
        raise ValueError("количество секунд не может быть отрицательным")
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main() -> None:
    cases = [0, 59, 60, 3661, 86399, 90061]
    for value in cases:
        print(f"{value:>6} с -> {seconds_to_hms(value)}")


if __name__ == "__main__":
    main()
