from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


@dataclass
class User:
    id: int
    name: str


T = TypeVar("T")


class Repository(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> None: ...

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]: ...

    @abstractmethod
    def find_all(self) -> list[T]: ...


class InMemoryUserRepository(Repository[User]):
    def __init__(self) -> None:
        self._storage: dict[int, User] = {}

    def add(self, entity: User) -> None:
        self._storage[entity.id] = entity

    def get_by_id(self, entity_id: int) -> Optional[User]:
        return self._storage.get(entity_id)

    def find_all(self) -> list[User]:
        return list(self._storage.values())


def main() -> None:
    repo: Repository[User] = InMemoryUserRepository()
    repo.add(User(1, "Alice"))
    repo.add(User(2, "Bob"))

    print("get_by_id(1):", repo.get_by_id(1))
    print("get_by_id(99):", repo.get_by_id(99))
    print("find_all:", repo.find_all())
    print("Клиент не знает о хранилище:", isinstance(repo, Repository))


if __name__ == "__main__":
    main()
