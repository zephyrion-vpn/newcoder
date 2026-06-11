VOWELS = set("aеiоуыэюяёаeouи")


def count_letters(word: str) -> tuple[int, int]:
    vowels = 0
    consonants = 0
    for char in word.lower():
        if not char.isalpha():
            continue
        if char in VOWELS:
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants


def main() -> None:
    word = input("Введите слово: ").strip()
    vowels, consonants = count_letters(word)
    print(f"Гласные: {vowels}")
    print(f"Согласные: {consonants}")


if __name__ == "__main__":
    main()
