from itertools import product


def password_combos(charset: str, length: int = 3) -> list[str]:
    return ["".join(combo) for combo in product(charset, repeat=length)]


def main() -> None:
    combos = password_combos("ab", 3)
    print(combos)
    print(f"Всего: {len(combos)}")
    print(f"Для 'abc' длины 3: {len(password_combos('abc', 3))} вариантов")


if __name__ == "__main__":
    main()
