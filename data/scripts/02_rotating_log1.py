import logging
import tempfile
from logging.handlers import RotatingFileHandler
from pathlib import Path


def build_logger(log_path: Path, max_bytes: int = 1024 * 1024, backups: int = 5) -> logging.Logger:
    logger = logging.getLogger("rotating_demo")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backups,
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    log_path = tmp / "app.log"
    # Небольшой порог для демонстрации ротации (в бое используйте 1 МБ).
    logger = build_logger(log_path, max_bytes=2048, backups=3)

    for i in range(500):
        logger.info("Событие номер %d — немного текста для объёма", i)

    rotated = sorted(p.name for p in tmp.iterdir())
    print("Созданные файлы логов:", rotated)
    print("Основной + ротированные копии (до backupCount).")
    print("Актуальный размер app.log:", log_path.stat().st_size, "байт")


if __name__ == "__main__":
    main()
