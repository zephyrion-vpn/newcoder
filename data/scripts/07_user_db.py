Users = dict[str, dict[str, object]]


def add_user(users: Users, user_id: str, name: str, age: int) -> None:
    users[user_id] = {"name": name, "age": age}


def find_by_name(users: Users, query: str) -> list[dict[str, object]]:
    needle = query.strip().lower()
    return [
        {"id": user_id, **info}
        for user_id, info in users.items()
        if needle in str(info["name"]).lower()
    ]


def main() -> None:
    users: Users = {}
    add_user(users, "u1", "Анна Петрова", 30)
    add_user(users, "u2", "Антон Иванов", 25)
    add_user(users, "u3", "Мария Сидорова", 28)
    for found in find_by_name(users, "ан"):
        print(found)
    print("---")
    print(find_by_name(users, "ззз"))


if __name__ == "__main__":
    main()
