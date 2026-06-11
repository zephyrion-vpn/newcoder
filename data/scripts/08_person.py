class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self._age = value

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def main() -> None:
    person = Person("Анна", "Петрова", 30)
    print(person.full_name)
    print(person.age)
    person.age = 31
    print(person.age)
    try:
        person.age = -5
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
