import logging
import os
import tempfile
from logging.handlers import RotatingFileHandler


def build_logger(path: str, max_bytes: int = 1_048_576, backups: int = 5) -> logging.Logger:
    logger = logging.getLogger(f"rotating:{path}")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backups, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def main() -> None:
    folder = tempfile.mkdtemp()
    path = os.path.join(folder, "app.log")
    logger = build_logger(path, max_bytes=1024, backups=3)
    for i in range(200):
        logger.info("Сообщение номер %d с дополнительным текстом для роста размера", i)
    created = sorted(name for name in os.listdir(folder) if name.startswith("app.log"))
    print(f"Создано файлов лога: {created}")


if __name__ == "__main__":
    main()
