import re

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def same_start_end(text: str) -> list[str]:
    result = []
    for match in WORD_PATTERN.finditer(text):
        word = match.group()
        if len(word) > 1 and word[0].lower() == word[-1].lower():
            result.append(word)
    return result


def main() -> None:
    text = "Анна ела кашу, level и radar всегда там. Кок и дед."
    print(same_start_end(text))


if __name__ == "__main__":
    main()
