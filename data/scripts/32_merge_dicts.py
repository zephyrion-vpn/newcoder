def main() -> None:
    first = {"a": 1, "b": 2}
    second = {"b": 3, "c": 4}
    merged = {**first, **second}
    print(f"Первый словарь: {first}")
    print(f"Второй словарь: {second}")
    print(f"Объединённый: {merged}")


if __name__ == "__main__":
    main()
