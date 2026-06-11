import json
import logging
import os
import tempfile
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_CONFIG: dict[str, Any] = {"host": "localhost", "port": 8080, "debug": False}


def read_config(path: str) -> dict[str, Any]:
    if not os.path.exists(path):
        logger.warning("Файл конфигурации не найден, создаю с настройками по умолчанию: %s", path)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(DEFAULT_CONFIG, handle, ensure_ascii=False, indent=4)
        return dict(DEFAULT_CONFIG)
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "config.json")
    print(read_config(path))
    print(read_config(path))


if __name__ == "__main__":
    main()
