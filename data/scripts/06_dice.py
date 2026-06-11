import random


class Dice:
    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("У кубика должно быть не меньше 2 граней.")
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


def main() -> None:
    random.seed(42)
    d6 = Dice()
    d20 = Dice(20)
    print(f"d6: {[d6.roll() for _ in range(5)]}")
    print(f"d20: {[d20.roll() for _ in range(5)]}")


if __name__ == "__main__":
    main()
