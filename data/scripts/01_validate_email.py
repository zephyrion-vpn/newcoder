import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    return EMAIL_PATTERN.fullmatch(email.strip()) is not None


def main() -> None:
    for email in ["user@example.com", "a.b@mail.co.uk", "bad@no", "@nope.com", "two@@x.com"]:
        print(f"{email}: {is_valid_email(email)}")


if __name__ == "__main__":
    main()
