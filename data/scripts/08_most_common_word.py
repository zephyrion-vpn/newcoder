import re
from collections import Counter

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def most_common_word(text: str) -> tuple[str, int] | None:
    words = [match.group().lower() for match in WORD_PATTERN.finditer(text)]
    if not words:
        return None
    return Counter(words).most_common(1)[0]


def main() -> None:
    text = "Кот сидит. Кот спит! А кот всё равно кот."
    print(most_common_word(text))


if __name__ == "__main__":
    main()
