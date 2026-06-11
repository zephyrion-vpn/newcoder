import logging
import os
import tempfile


def setup_logging(error_log: str) -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(console)

    file_handler = logging.FileHandler(error_log, encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
    logger.addHandler(file_handler)
    return logger


def main() -> None:
    error_log = os.path.join(tempfile.mkdtemp(), "errors.log")
    logger = setup_logging(error_log)
    logger.info("Информационное сообщение (только в консоль)")
    logger.error("Ошибка (консоль + файл)")
    print("--- содержимое errors.log ---")
    with open(error_log, encoding="utf-8") as handle:
        print(handle.read().strip())


if __name__ == "__main__":
    main()
