import re

_CHARACTER_CLASSES = (
    re.compile(r"[a-zа-яё]"),
    re.compile(r"[A-ZА-ЯЁ]"),
    re.compile(r"\d"),
    re.compile(r"[^\w]"),
)
_COMMON_PASSWORDS = frozenset(
    {
        "password",
        "qwerty",
        "123456",
        "12345678",
        "111111",
        "admin",
        "letmein",
        "welcome",
        "iloveyou",
        "пароль",
    }
)


def _contains_common_word(password: str) -> bool:
    lowered = password.lower()
    return any(common in lowered for common in _COMMON_PASSWORDS)


def password_strength(password: str) -> int:
    if not password:
        return 1
    length_score = 2 if len(password) >= 12 else 1 if len(password) >= 8 else 0
    classes = sum(bool(pattern.search(password)) for pattern in _CHARACTER_CLASSES)
    variety_score = min(max(classes - 1, 0), 2)
    score = 1 + length_score + variety_score
    if _contains_common_word(password):
        score = min(score, 2)
    return max(1, min(score, 5))


def main() -> None:
    samples = ("123456", "qwerty123", "Sun*flower", "Tr0ub4dor&3xZ!")
    for password in samples:
        print(f"{password!r}: {password_strength(password)}/5")


if __name__ == "__main__":
    main()
