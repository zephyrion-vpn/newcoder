class InvalidAgeError(Exception):
    def __init__(self, age: int) -> None:
        super().__init__(f"Недопустимый возраст: {age}. Допустимый диапазон 0–120.")
        self.age = age


def register(name: str, age: int) -> str:
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return f"Пользователь {name} ({age}) зарегистрирован."


def main() -> None:
    print(register("Анна", 30))
    for age in (-5, 150):
        try:
            register("Тест", age)
        except InvalidAgeError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
