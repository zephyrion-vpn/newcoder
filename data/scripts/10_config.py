from typing import Any


class Config:
    def __init__(self, settings: dict[str, Any]) -> None:
        object.__setattr__(self, "_settings", dict(settings))

    def __getattr__(self, name: str) -> Any:
        try:
            return self._settings[name]
        except KeyError:
            raise AttributeError(f"Настройка {name!r} не найдена.") from None


def main() -> None:
    config = Config({"host": "localhost", "port": 8080, "debug": True})
    print(config.host)
    print(config.port)
    print(config.debug)
    try:
        print(config.missing)
    except AttributeError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
