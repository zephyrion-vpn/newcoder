def normalize(text: str) -> list[str]:
    return sorted(char for char in text.lower() if char.isalnum())


def are_anagrams(first: str, second: str) -> bool:
    return normalize(first) == normalize(second)


def main() -> None:
    print(are_anagrams("листок", "столик"))
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))


if __name__ == "__main__":
    main()
