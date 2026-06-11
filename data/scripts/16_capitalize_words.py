def capitalize_words(sentence: str) -> str:
    return " ".join(word[:1].upper() + word[1:] for word in sentence.split(" "))


def main() -> None:
    sentence = input("Введите предложение: ")
    print(capitalize_words(sentence))


if __name__ == "__main__":
    main()
