class InvalidEmailError(Exception):
    pass


ALLOWED_ZONES = (".com", ".ru", ".org")


def validate_email(email: str) -> str:
    email = email.strip()
    if email.count("@") != 1:
        raise InvalidEmailError("Адрес должен содержать ровно один символ @.")
    local, _, domain = email.partition("@")
    if not local or not domain:
        raise InvalidEmailError("Локальная часть и домен не могут быть пустыми.")
    if not domain.lower().endswith(ALLOWED_ZONES):
        raise InvalidEmailError(f"Домен должен оканчиваться на одну из зон: {', '.join(ALLOWED_ZONES)}.")
    return email


def main() -> None:
    for email in ("user@example.com", "user@site.ru", "bad-email", "user@site.net"):
        try:
            validate_email(email)
            print(f"{email!r}: OK")
        except InvalidEmailError as error:
            print(f"{email!r}: {error}")


if __name__ == "__main__":
    main()
