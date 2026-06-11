import secrets
import string

CAPTCHA_LENGTH = 6
ALPHABET = string.ascii_letters + string.digits


def generate_captcha(length: int = CAPTCHA_LENGTH) -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main() -> None:
    print(f"Капча: {generate_captcha()}")


if __name__ == "__main__":
    main()
