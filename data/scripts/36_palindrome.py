def is_palindrome(text: str) -> bool:
    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome("level"))
