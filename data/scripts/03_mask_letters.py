VOWELS = set("aeiouаеёиоуыэюя")


def mask_letters(text: str) -> str:
    result = []
    for char in text:
        if char.isalpha():
            result.append("*" if char.lower() in VOWELS else "#")
        else:
            result.append(char)
    return "".join(result)


def main() -> None:
    print(mask_letters("Привет, мир!"))
    print(mask_letters("Hello World 123"))


if __name__ == "__main__":
    main()
