import json
import os
import tempfile
from typing import Any


def add_user(path: str, user: dict[str, Any]) -> int:
    with open(path, encoding="utf-8") as handle:
        users = json.load(handle)
    if not isinstance(users, list):
        raise ValueError("Ожидался список пользователей.")
    users.append(user)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(users, handle, ensure_ascii=False, indent=4)
    return len(users)


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "users.json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump([{"id": 1, "name": "Анна"}], handle, ensure_ascii=False, indent=4)
    total = add_user(path, {"id": 2, "name": "Борис"})
    print(f"Всего пользователей: {total}")
    with open(path, encoding="utf-8") as handle:
        print(handle.read())


if __name__ == "__main__":
    main()
