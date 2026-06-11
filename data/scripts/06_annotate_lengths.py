import re

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def annotate_lengths(text: str) -> str:
    return WORD_PATTERN.sub(lambda m: f"{m.group()} ({len(m.group())})", text)


def main() -> None:
    print(annotate_lengths("Привет мир"))
    print(annotate_lengths("Hello, world!"))


if __name__ == "__main__":
    main()
