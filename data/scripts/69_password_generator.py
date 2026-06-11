import secrets
import string


def generate_password(length: int = 8) -> str:
    if length < 3:
        raise ValueError("Длина пароля должна быть не меньше 3.")
    categories = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    alphabet = "".join(categories)
    while True:
        password = [secrets.choice(category) for category in categories]
        password += [secrets.choice(alphabet) for _ in range(length - len(categories))]
        secrets.SystemRandom().shuffle(password)
        return "".join(password)


def main() -> None:
    print(generate_password())


if __name__ == "__main__":
    main()
