class InvalidAgeError(Exception):
    def __init__(self, age: int) -> None:
        super().__init__(f"Недопустимый возраст: {age}")
        self.age = age


def register(name: str, age: int) -> dict[str, object]:
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return {"name": name, "age": age}


def main() -> None:
    print(register("Анна", 30))
    for age in (-5, 200):
        try:
            register("Тест", age)
        except InvalidAgeError as error:
            print("Перехвачено:", error)


if __name__ == "__main__":
    main()
