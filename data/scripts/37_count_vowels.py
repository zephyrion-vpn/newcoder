def count_vowels(text: str) -> int:
    return sum(char in "aeiou" for char in text.lower())


if __name__ == "__main__":
    print(count_vowels("hello"))
