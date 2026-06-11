from typing import Any


class ValidationError(Exception):
    pass


def validate_schema(data: dict[str, Any], schema: dict[str, type]) -> None:
    for key, expected_type in schema.items():
        if key not in data:
            raise ValidationError(f"Отсутствует обязательный ключ: {key!r}.")
        value = data[key]
        if expected_type is not bool and isinstance(value, bool):
            raise ValidationError(f"Ключ {key!r}: ожидался {expected_type.__name__}, получен bool.")
        if not isinstance(value, expected_type):
            raise ValidationError(
                f"Ключ {key!r}: ожидался {expected_type.__name__}, получен {type(value).__name__}."
            )


def main() -> None:
    schema = {"name": str, "age": int, "active": bool}
    print("Валидный:", end=" ")
    try:
        validate_schema({"name": "Анна", "age": 30, "active": True}, schema)
        print("OK")
    except ValidationError as error:
        print(error)
    for bad in ({"name": "Анна", "active": True}, {"name": "Анна", "age": "30", "active": True}):
        try:
            validate_schema(bad, schema)
        except ValidationError as error:
            print(f"ValidationError: {error}")


if __name__ == "__main__":
    main()
