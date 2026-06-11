def read_people(prompt: str) -> dict[str, int]:
    print(prompt)
    print("Формат строки: Имя Возраст. Пустая строка завершает ввод.")
    people: dict[str, int] = {}
    while True:
        line = input("> ").strip()
        if not line:
            break
        parts = line.rsplit(maxsplit=1)
        if len(parts) != 2:
            print("Введите имя и возраст через пробел.")
            continue
        name, raw_age = parts
        try:
            people[name] = int(raw_age)
        except ValueError:
            print("Возраст должен быть целым числом.")
    return people


def main() -> None:
    people = read_people("Введите людей:")
    adults = [name for name, age in people.items() if age > 18]
    print(f"Старше 18: {adults}" if adults else "Нет людей старше 18.")


if __name__ == "__main__":
    main()
