class Base:
    def process(self) -> list[str]:
        return ["Base"]


class Left(Base):
    def process(self) -> list[str]:
        return ["Left", *super().process()]


class Right(Base):
    def process(self) -> list[str]:
        return ["Right", *super().process()]


class Diamond(Left, Right):
    def process(self) -> list[str]:
        return ["Diamond", *super().process()]


def main() -> None:
    print("MRO (C3 linearization):")
    for cls in Diamond.__mro__:
        print(f"  {cls.__name__}")
    print("Порядок вызовов process():", " -> ".join(Diamond().process()))


if __name__ == "__main__":
    main()
