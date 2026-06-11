from itertools import permutations
from typing import Iterator


def string_permutations(text: str) -> Iterator[str]:
    for combo in permutations(text):
        yield "".join(combo)


def main() -> None:
    print(list(string_permutations("abc")))
    print(f"Количество для 'abcd': {sum(1 for _ in string_permutations('abcd'))}")


if __name__ == "__main__":
    main()
