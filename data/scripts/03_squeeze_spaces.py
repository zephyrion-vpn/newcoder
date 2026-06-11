import re

SPACES_PATTERN = re.compile(r" +")


def squeeze_spaces(text: str) -> str:
    return SPACES_PATTERN.sub(" ", text)


def main() -> None:
    print(repr(squeeze_spaces("Привет    мир,   как    дела?")))
    print(repr(squeeze_spaces("без лишних пробелов")))


if __name__ == "__main__":
    main()
