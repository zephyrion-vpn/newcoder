import re

PHONE_PATTERN = re.compile(r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}|8-\d{3}-\d{3}-\d{2}-\d{2}")


def extract_phones(text: str) -> list[str]:
    return PHONE_PATTERN.findall(text)


def main() -> None:
    text = (
        "Свяжитесь: +7 (495) 123-45-67 или 8-800-555-35-35. "
        "Неверный: 12345, +7 495 1234567."
    )
    print(extract_phones(text))


if __name__ == "__main__":
    main()
