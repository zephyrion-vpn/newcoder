import inspect
from typing import Callable, TypeVar

T = TypeVar("T")


class Container:
    def __init__(self) -> None:
        self._factories: dict[type, Callable[..., object]] = {}
        self._singletons: dict[type, object] = {}
        self._instances: dict[type, object] = {}

    def register(self, interface: type, factory: Callable[..., object], singleton: bool = False) -> None:
        self._factories[interface] = factory
        if singleton:
            self._singletons[interface] = None

    def resolve(self, interface: type[T]) -> T:
        if interface in self._singletons and self._instances.get(interface) is not None:
            return self._instances[interface]  # type: ignore[return-value]

        factory = self._factories.get(interface)
        if factory is None:
            raise KeyError(f"Не зарегистрировано: {interface}")

        kwargs = {}
        signature = inspect.signature(factory)
        for name, param in signature.parameters.items():
            if param.annotation in self._factories:
                kwargs[name] = self.resolve(param.annotation)
        instance = factory(**kwargs)

        if interface in self._singletons:
            self._instances[interface] = instance
        return instance  # type: ignore[return-value]


class Database:
    def query(self) -> str:
        return "данные из БД"


class UserService:
    def __init__(self, db: Database) -> None:
        self.db = db

    def get_users(self) -> str:
        return f"UserService -> {self.db.query()}"


def main() -> None:
    container = Container()
    container.register(Database, Database, singleton=True)
    container.register(UserService, UserService)

    service = container.resolve(UserService)
    print(service.get_users())

    db1 = container.resolve(Database)
    db2 = container.resolve(Database)
    print(f"Database — singleton: {db1 is db2}")
    print(f"db внутри service — тот же: {service.db is db1}")


if __name__ == "__main__":
    main()
