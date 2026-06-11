import json
import logging
import tempfile
from pathlib import Path
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("config")

DEFAULT_CONFIG: dict[str, Any] = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "retries": 3,
}


def read_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        logger.warning("Файл конфигурации %s не найден, создаю с настройками по умолчанию.", path)
        path.write_text(json.dumps(DEFAULT_CONFIG, ensure_ascii=False, indent=2), encoding="utf-8")
        return dict(DEFAULT_CONFIG)
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    config_path = tmp / "config.json"

    print("Первый вызов (файла нет):")
    first = read_config(config_path)
    print("   Получено:", first)
    print(f"   Файл создан: {config_path.exists()}")

    print("\nВторой вызов (файл уже есть):")
    second = read_config(config_path)
    print("   Получено:", second)


if __name__ == "__main__":
    main()
