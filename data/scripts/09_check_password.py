import re


def is_strong(password: str) -> bool:
    return bool(
        re.search(r"[A-ZА-ЯЁ]", password)
        and re.search(r"[a-zа-яё]", password)
        and re.search(r"\d", password)
    )


def main() -> None:
    for password in ["Abc123", "abc123", "ABC123", "Abcdef", "Пароль1"]:
        print(f"{password}: {is_strong(password)}")


if __name__ == "__main__":
    main()
