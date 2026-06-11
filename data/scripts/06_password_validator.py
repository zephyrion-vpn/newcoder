class PasswordError(Exception):
    pass


class ShortPasswordError(PasswordError):
    pass


class NoDigitError(PasswordError):
    pass


def validate_password(password: str, min_length: int = 8) -> None:
    if len(password) < min_length:
        raise ShortPasswordError(f"Пароль короче {min_length} символов.")
    if not any(char.isdigit() for char in password):
        raise NoDigitError("Пароль должен содержать хотя бы одну цифру.")


def main() -> None:
    for password in ("abc", "abcdefgh", "abcdef12"):
        try:
            validate_password(password)
            print(f"{password!r}: OK")
        except PasswordError as error:
            print(f"{password!r}: {type(error).__name__} — {error}")


if __name__ == "__main__":
    main()
