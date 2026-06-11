import logging
from typing import Any

logger = logging.getLogger(__name__)


def nested_get(data: dict, keys: list) -> Any | None:
    current: Any = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            logger.warning("Ключ %r не найден в пути %s", key, keys)
            return None
    return current


def main() -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    data = {"user": {"profile": {"name": "Анна", "age": 30}}}
    print("name ->", nested_get(data, ["user", "profile", "name"]))
    print("city ->", nested_get(data, ["user", "profile", "city"]))
    print("глубоко ->", nested_get(data, ["user", "settings", "theme"]))


if __name__ == "__main__":
    main()
