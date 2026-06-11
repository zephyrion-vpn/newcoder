from typing import Any


class ValidationError(Exception):
    pass


def validate_schema(data: dict[str, Any], schema: dict[str, type | tuple[type, ...]]) -> None:
    if not isinstance(data, dict):
        raise ValidationError("данные должны быть словарём")
    for key, expected in schema.items():
        if key not in data:
            raise ValidationError(f"отсутствует ключ: {key!r}")
        value = data[key]
        if expected is float and isinstance(value, int) and not isinstance(value, bool):
            continue
        if isinstance(value, bool) and expected is not bool:
            raise ValidationError(f"ключ {key!r}: ожидался {expected}, получен bool")
        if not isinstance(value, expected):
            got = type(value).__name__
            raise ValidationError(f"ключ {key!r}: ожидался {expected}, получен {got}")


def main() -> None:
    schema = {"name": str, "age": int, "score": float, "active": bool}

    valid = {"name": "Alice", "age": 30, "score": 9.5, "active": True}
    try:
        validate_schema(valid, schema)
        print("✓ Валидный словарь прошёл проверку.")
    except ValidationError as error:
        print(f"✗ {error}")

    bad_cases = [
        {"name": "Bob", "age": "тридцать", "score": 9.5, "active": True},
        {"name": "Carol", "age": 25, "score": 8.0},
        {"name": "Dave", "age": True, "score": 8.0, "active": False},
    ]
    for case in bad_cases:
        try:
            validate_schema(case, schema)
            print(f"✓ {case}")
        except ValidationError as error:
            print(f"✗ {error}")


if __name__ == "__main__":
    main()
