def sort_people(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda person: (-person["age"], person["name"]))


def main() -> None:
    people = [
        {"name": "Анна", "age": 30},
        {"name": "Борис", "age": 25},
        {"name": "Вера", "age": 30},
        {"name": "Глеб", "age": 25},
    ]
    for person in sort_people(people):
        print(person)


if __name__ == "__main__":
    main()
