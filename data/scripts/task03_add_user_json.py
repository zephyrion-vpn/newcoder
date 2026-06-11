import json
import os
import tempfile
from typing import Any


def add_user(path: str, user: dict[str, Any]) -> int:
    try:
        with open(path, encoding="utf-8") as handle:
            users = json.load(handle)
    except FileNotFoundError:
        users = []
    if not isinstance(users, list):
        raise ValueError("Ожидался список пользователей")
    users.append(user)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(users, handle, indent=4, ensure_ascii=False)
    return len(users)


def main() -> None:
    path = tempfile.mktemp(suffix=".json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump([{"id": 1, "name": "Алиса"}], handle, ensure_ascii=False)
    total = add_user(path, {"id": 2, "name": "Боб"})
    print(f"Всего пользователей: {total}")
    with open(path, encoding="utf-8") as handle:
        print(handle.read())
    os.remove(path)


if __name__ == "__main__":
    main()
