def longest_word(sentence: str) -> str | None:
    words = sentence.split()
    return max(words, key=len) if words else None


def main() -> None:
    sentence = input("Введите предложение: ")
    word = longest_word(sentence)
    if word is None:
        print("Предложение пустое.")
    else:
        print(f"Самое длинное слово: {word}")


if __name__ == "__main__":
    main()
