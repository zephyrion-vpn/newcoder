def is_palindrome(word: str) -> bool:
    normalized = "".join(char for char in word.lower() if char.isalnum())
    return bool(normalized) and normalized == normalized[::-1]


def main() -> None:
    word = input("Введите слово: ").strip()
    if is_palindrome(word):
        print("Это палиндром.")
    else:
        print("Это не палиндром.")


if __name__ == "__main__":
    main()
