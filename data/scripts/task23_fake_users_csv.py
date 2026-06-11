import csv
import os
import random
import tempfile

try:
    from faker import Faker

    _faker: "Faker | None" = Faker()
except ImportError:
    _faker = None

_FIRST = ["Anna", "Ivan", "Olga", "Petr", "Maria", "Sergey", "Elena", "Dmitry"]
_LAST = ["Ivanov", "Petrov", "Sidorov", "Smirnov", "Volkov", "Orlov"]
_DOMAINS = ["example.com", "mail.test", "demo.org"]


def generate_users(count: int) -> list[dict[str, object]]:
    users: list[dict[str, object]] = []
    for _ in range(count):
        if _faker is not None:
            users.append(
                {
                    "name": _faker.name(),
                    "email": _faker.email(),
                    "age": random.randint(18, 80),
                }
            )
        else:
            first = random.choice(_FIRST)
            last = random.choice(_LAST)
            users.append(
                {
                    "name": f"{first} {last}",
                    "email": f"{first.lower()}.{last.lower()}{random.randint(1, 99)}@{random.choice(_DOMAINS)}",
                    "age": random.randint(18, 80),
                }
            )
    return users


def save_csv(users: list[dict[str, object]], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["name", "email", "age"])
        writer.writeheader()
        writer.writerows(users)


def main() -> None:
    source = "Faker" if _faker is not None else "собственные списки"
    print(f"Источник данных: {source}")
    users = generate_users(100)
    path = tempfile.mktemp(suffix=".csv")
    save_csv(users, path)
    print(f"Сохранено пользователей: {len(users)}")
    print("Примеры:")
    for user in users[:3]:
        print(" ", user)
    os.remove(path)


if __name__ == "__main__":
    main()
