import logging


def configure_logging(error_file: str = "errors.log") -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(error_file, encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger


def main() -> None:
    logger = configure_logging()
    logger.info("Это информация — только в консоль")
    logger.warning("Это предупреждение — только в консоль")
    logger.error("Это ошибка — в консоль и в errors.log")
    print("Готово: см. файл errors.log для записей уровня ERROR")


if __name__ == "__main__":
    main()
