class PasswordError(Exception):
    pass


class ShortPasswordError(PasswordError):
    pass


class NoDigitError(PasswordError):
    pass


def validate_password(password: str, min_length: int = 8) -> None:
    if len(password) < min_length:
        raise ShortPasswordError(f"Пароль короче {min_length} символов")
    if not any(char.isdigit() for char in password):
        raise NoDigitError("Пароль должен содержать хотя бы одну цифру")


def main() -> None:
    for password in ("abc", "abcdefgh", "abcd1234"):
        try:
            validate_password(password)
        except ShortPasswordError as error:
            print(f"{password!r}: короткий — {error}")
        except NoDigitError as error:
            print(f"{password!r}: без цифр — {error}")
        else:
            print(f"{password!r}: пароль корректен")


if __name__ == "__main__":
    main()
