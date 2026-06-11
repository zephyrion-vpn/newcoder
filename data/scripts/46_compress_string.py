from itertools import groupby


def compress(text: str) -> str:
    return "".join(f"{char}{len(list(group))}" for char, group in groupby(text))


def main() -> None:
    print(compress("aaabb"))


if __name__ == "__main__":
    main()
