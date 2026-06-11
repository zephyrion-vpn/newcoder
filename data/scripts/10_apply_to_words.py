import re
from typing import Callable

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def apply_to_words(text: str, transform: Callable[[str], str]) -> str:
    return WORD_PATTERN.sub(lambda m: transform(m.group()), text)


def main() -> None:
    print(apply_to_words("привет мир", str.upper))
    print(apply_to_words("Hello World", str.lower))
    print(apply_to_words("каждое слово с большой", str.capitalize))


if __name__ == "__main__":
    main()
