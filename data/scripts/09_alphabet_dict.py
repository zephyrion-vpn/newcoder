from string import ascii_lowercase


def alphabet_positions() -> dict[str, int]:
    return {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}


def main() -> None:
    mapping = alphabet_positions()
    print(mapping)
    print(mapping["a"], mapping["z"])


if __name__ == "__main__":
    main()
