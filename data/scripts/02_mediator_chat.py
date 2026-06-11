from __future__ import annotations

from abc import ABC, abstractmethod


class ChatMediator(ABC):
    @abstractmethod
    def broadcast(self, sender: "User", message: str) -> None: ...

    @abstractmethod
    def register(self, user: "User") -> None: ...


class ChatRoom(ChatMediator):
    def __init__(self) -> None:
        self._users: list[User] = []
        self.log: list[str] = []

    def register(self, user: "User") -> None:
        self._users.append(user)
        user.room = self

    def broadcast(self, sender: "User", message: str) -> None:
        for user in self._users:
            if user is not sender:
                user.receive(sender.name, message)
        self.log.append(f"{sender.name}: {message}")


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.room: ChatMediator | None = None
        self.inbox: list[str] = []

    def send(self, message: str) -> None:
        if self.room is None:
            raise RuntimeError("Пользователь не в комнате.")
        self.room.broadcast(self, message)

    def receive(self, sender_name: str, message: str) -> None:
        self.inbox.append(f"{sender_name}: {message}")


def main() -> None:
    room = ChatRoom()
    alice, bob, carol = User("Alice"), User("Bob"), User("Carol")
    for user in (alice, bob, carol):
        room.register(user)

    alice.send("Привет всем!")
    bob.send("Привет, Alice!")

    print("Inbox Bob:", bob.inbox)
    print("Inbox Carol:", carol.inbox)
    print("Inbox Alice:", alice.inbox)
    print("Журнал комнаты:", room.log)


if __name__ == "__main__":
    main()
