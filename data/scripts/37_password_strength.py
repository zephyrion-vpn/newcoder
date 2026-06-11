import re

COMMON_WORDS = {
    "password", "qwerty", "123456", "admin", "welcome", "letmein",
    "пароль", "йцукен", "админ",
}


def password_strength(password: str) -> tuple[int, list[str]]:
    notes: list[str] = []
    score = 0
    lowered = password.lower()

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        notes.append("слишком короткий (<8)")

    variety = sum(bool(re.search(p, password)) for p in (r"[a-zа-я]", r"[A-ZА-Я]", r"\d", r"[^\w\s]"))
    score += variety - 1 if variety > 0 else 0
    if variety < 3:
        notes.append("мало типов символов")

    if any(word in lowered for word in COMMON_WORDS):
        score = max(score - 2, 0)
        notes.append("содержит словарное слово")

    score = max(1, min(score, 5))
    return score, notes


def main() -> None:
    samples = ["123456", "password1", "Qwerty12", "S3cur3!Pass", "X9$kL2#mZq7@vR4!"]
    for pwd in samples:
        score, notes = password_strength(pwd)
        bar = "█" * score + "░" * (5 - score)
        note_str = f" ({', '.join(notes)})" if notes else ""
        print(f"{pwd:<20} [{bar}] {score}/5{note_str}")


if __name__ == "__main__":
    main()
