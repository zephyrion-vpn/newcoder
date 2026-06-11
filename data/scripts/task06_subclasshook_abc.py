from abc import ABC


class Duck(ABC):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool | type(NotImplemented):
        if cls is Duck:
            if any("quack" in vars(klass) for klass in subclass.__mro__):
                return True
            return NotImplemented
        return NotImplemented


class MallardDuck:
    def quack(self) -> str:
        return "Кря-кря"


class Dog:
    def bark(self) -> str:
        return "Гав"


def main() -> None:
    print("MallardDuck — подкласс Duck?", issubclass(MallardDuck, Duck))
    print("MallardDuck() — экземпляр Duck?", isinstance(MallardDuck(), Duck))
    print("Dog — подкласс Duck?", issubclass(Dog, Duck))


if __name__ == "__main__":
    main()
