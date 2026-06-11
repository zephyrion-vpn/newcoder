import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def safe_int(value: str) -> int:
    try:
        return int(value)
    except (ValueError, TypeError) as error:
        logger.error("Не удалось преобразовать %r в int: %s", value, error)
        return 0


def main() -> None:
    print(safe_int("42"))
    print(safe_int("не число"))
    print(safe_int(None))  # type: ignore[arg-type]


if __name__ == "__main__":
    main()
