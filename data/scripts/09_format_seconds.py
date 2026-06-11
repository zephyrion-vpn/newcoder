def format_seconds(seconds: int) -> str:
    if seconds < 0:
        raise ValueError("Количество секунд не может быть отрицательным.")
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def main() -> None:
    for value in (0, 59, 3661, 86399):
        print(f"{value} → {format_seconds(value)}")


if __name__ == "__main__":
    main()
