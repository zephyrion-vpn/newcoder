import logging
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def safe_get(data: dict[str, Any], keys: list[str]) -> Any:
    current: Any = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            logger.warning("Ключ %r не найден в пути %s", key, keys)
            return None
    return current


def main() -> None:
    data = {"user": {"profile": {"name": "Анна", "age": 30}}}
    print(safe_get(data, ["user", "profile", "name"]))
    print(safe_get(data, ["user", "profile", "email"]))
    print(safe_get(data, ["user", "settings", "theme"]))


if __name__ == "__main__":
    main()
