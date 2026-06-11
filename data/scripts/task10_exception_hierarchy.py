import logging

logger = logging.getLogger("app")


class LoggingMixin:
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        logger.error("%s: %s", type(self).__name__, self)


class BaseAppError(LoggingMixin, Exception):
    pass


class ValidationError(BaseAppError):
    pass


class DatabaseError(BaseAppError):
    pass


class NotFoundError(DatabaseError):
    pass


def main() -> None:
    logging.basicConfig(level=logging.ERROR, format="[LOG] %(name)s: %(message)s")
    for exception_type in (ValidationError, NotFoundError):
        try:
            raise exception_type("что-то пошло не так")
        except BaseAppError as error:
            print(f"Поймано: {type(error).__name__} -> {error}")


if __name__ == "__main__":
    main()
