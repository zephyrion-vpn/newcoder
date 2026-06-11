class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> str:
        raise NotImplementedError("Подкласс должен переопределить make_sound.")

    def __str__(self) -> str:
        return f"{self.name}: {self.make_sound()}"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Гав"


class Cat(Animal):
    def make_sound(self) -> str:
        return "Мяу"


def main() -> None:
    animals = [Dog("Бобик"), Cat("Мурка")]
    for animal in animals:
        print(animal)


if __name__ == "__main__":
    main()
