import logging

logger = logging.getLogger(__name__)


def to_int(value: str) -> int:
    try:
        return int(value)
    except (ValueError, TypeError) as error:
        logger.error("Не удалось преобразовать %r в int: %s", value, error)
        return 0


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    print("'42' ->", to_int("42"))
    print("'abc' ->", to_int("abc"))
    print("None ->", to_int(None))


if __name__ == "__main__":
    main()
