from __future__ import annotations

from copy import deepcopy


class Database:
    def __init__(self) -> None:
        self.committed: dict[int, str] = {}


class UnitOfWork:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._staging: dict[int, str] = {}
        self._snapshot: dict[int, str] = {}

    def __enter__(self) -> "UnitOfWork":
        self._snapshot = deepcopy(self._db.committed)
        self._staging = deepcopy(self._db.committed)
        return self

    def register_new(self, entity_id: int, value: str) -> None:
        self._staging[entity_id] = value

    def register_deleted(self, entity_id: int) -> None:
        self._staging.pop(entity_id, None)

    def commit(self) -> None:
        self._db.committed = deepcopy(self._staging)

    def rollback(self) -> None:
        self._staging = deepcopy(self._snapshot)

    def __exit__(self, exc_type, exc, tb) -> bool:
        if exc_type is not None:
            self.rollback()
            print(f"Откат из-за ошибки: {exc_type.__name__}")
        return False


def main() -> None:
    db = Database()
    db.committed = {1: "Alice"}

    with UnitOfWork(db) as uow:
        uow.register_new(2, "Bob")
        uow.register_new(3, "Carol")
        uow.commit()
    print("После успешного commit:", db.committed)

    try:
        with UnitOfWork(db) as uow:
            uow.register_new(4, "Dave")
            raise ValueError("сбой в середине транзакции")
            uow.commit()
    except ValueError:
        pass
    print("После отката (Dave не должен появиться):", db.committed)


if __name__ == "__main__":
    main()
