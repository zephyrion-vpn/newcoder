from collections import Counter


def can_build(target: str, available: str) -> bool:
    return not (Counter(target) - Counter(available))


def main() -> None:
    print(can_build("кот", "токрыша"))
    print(can_build("коты", "кот"))
    print(can_build("book", "bok"))
    print(can_build("book", "boko"))
    print(can_build("", "abc"))


if __name__ == "__main__":
    main()
