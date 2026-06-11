class Base:
    def greet(self) -> str:
        return "Base"


class A(Base):
    def greet(self) -> str:
        return "A"


class B(Base):
    def greet(self) -> str:
        return "B"


class Child(A):
    pass


def main() -> None:
    obj = Child()
    print("Исходный greet():", obj.greet())
    print("Исходный MRO:", [cls.__name__ for cls in Child.__mro__])

    # __mro__ доступен только для чтения, но __bases__ можно переназначить.
    # Это перестраивает MRO и меняет разрешение методов на лету.
    Child.__bases__ = (B,)
    print("\nПосле Child.__bases__ = (B,):")
    print("Новый greet():", obj.greet())
    print("Новый MRO:", [cls.__name__ for cls in Child.__mro__])

    print(
        "\nРиски: подмена __bases__ может сломать раскладку памяти экземпляров,\n"
        "привести к TypeError (несовместимый layout), нарушить инварианты C3-линеаризации\n"
        "и сделать код непредсказуемым. Использовать только осознанно."
    )


if __name__ == "__main__":
    main()
