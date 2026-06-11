import re

ALLOWED_TLDS = (".com", ".ru", ".org")
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class InvalidEmailError(ValueError):
    pass


def validate_email(address: str) -> str:
    if not isinstance(address, str) or not address.strip():
        raise InvalidEmailError("адрес пуст")
    address = address.strip()
    if "@" not in address:
        raise InvalidEmailError("отсутствует символ '@'")
    if not _EMAIL_RE.match(address):
        raise InvalidEmailError("неверный формат адреса")
    domain = address.rsplit("@", 1)[1].lower()
    if not domain.endswith(ALLOWED_TLDS):
        raise InvalidEmailError(f"доменная зона должна быть одной из {ALLOWED_TLDS}")
    return address


def main() -> None:
    samples = [
        "user@example.com",
        "иван@mail.ru",
        "team@project.org",
        "no-at-sign.com",
        "user@site.net",
        "user@@bad.com",
    ]
    for address in samples:
        try:
            validate_email(address)
            print(f"✓ {address}")
        except InvalidEmailError as error:
            print(f"✗ {address} — {error}")


if __name__ == "__main__":
    main()
