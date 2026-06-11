import types
from typing import TypeVar

T = TypeVar("T", bound=type)


def privatize_methods(cls: T) -> T:
    renamed: dict[str, types.FunctionType] = {}
    for name, attribute in list(vars(cls).items()):
        if isinstance(attribute, types.FunctionType) and not name.startswith("_"):
            renamed[name] = attribute
    for name, attribute in renamed.items():
        setattr(cls, f"_{name}", attribute)
        delattr(cls, name)
    return cls


@privatize_methods
class Service:
    def connect(self) -> str:
        return "подключено"

    def fetch(self) -> str:
        return "данные"

    def __len__(self) -> int:
        return 0


def main() -> None:
    service = Service()
    print("Публичные методы стали:", [n for n in vars(Service) if not n.startswith("__")])
    print(service._connect())
    print(service._fetch())


if __name__ == "__main__":
    main()
