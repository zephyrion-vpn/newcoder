from typing import Any

registry: dict[str, type] = {}


class RegistryMeta(type):
    def __new__(
        mcs, name: str, bases: tuple[type, ...], namespace: dict[str, Any], **kwargs: Any
    ) -> type:
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        registry[name] = cls
        return cls


class Plugin(metaclass=RegistryMeta):
    pass


class JsonExporter(Plugin):
    pass


class CsvExporter(Plugin):
    pass


def main() -> None:
    print("Зарегистрированные классы:")
    for name, cls in registry.items():
        print(f"  {name} -> {cls.__module__}.{cls.__qualname__}")


if __name__ == "__main__":
    main()
