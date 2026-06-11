from collections import Counter


def char_frequency(text: str) -> dict[str, int]:
    return dict(Counter(text))


def main() -> None:
    print(char_frequency("миссисипи"))
    print(char_frequency("hello world"))
    print(char_frequency(""))


if __name__ == "__main__":
    main()
