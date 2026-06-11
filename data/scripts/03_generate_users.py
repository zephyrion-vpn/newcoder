import csv
import random
import tempfile
from pathlib import Path

try:
    from faker import Faker  # type: ignore
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False

FIRST_NAMES = ["Анна", "Иван", "Мария", "Пётр", "Елена", "Сергей", "Ольга", "Дмитрий"]
LAST_NAMES = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов"]
DOMAINS = ["example.com", "mail.ru", "test.org"]


def generate_users(count: int) -> list[dict[str, object]]:
    users: list[dict[str, object]] = []
    if HAS_FAKER:
        fake = Faker("ru_RU")
        for _ in range(count):
            name = fake.name()
            users.append({"name": name, "email": fake.email(), "age": random.randint(18, 80)})
        return users
    for i in range(count):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        email = f"{_translit(first)}.{_translit(last)}{i}@{random.choice(DOMAINS)}".lower()
        users.append({"name": f"{first} {last}", "email": email, "age": random.randint(18, 80)})
    return users


def _translit(text: str) -> str:
    table = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
        "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
        "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
        "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "", "э": "e",
        "ю": "yu", "я": "ya",
    }
    return "".join(table.get(ch, ch) for ch in text.lower())


def save_csv(users: list[dict[str, object]], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["name", "email", "age"])
        writer.writeheader()
        writer.writerows(users)


def main() -> None:
    users = generate_users(100)
    path = Path(tempfile.mkdtemp()) / "users.csv"
    save_csv(users, path)
    print(f"Faker доступен: {HAS_FAKER}")
    print(f"Создано пользователей: {len(users)} → {path}")
    print("Пример:", users[0])


if __name__ == "__main__":
    main()
