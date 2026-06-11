from __future__ import annotations

from copy import deepcopy


class GameMemento:
    def __init__(self, state: dict) -> None:
        self._state = deepcopy(state)

    def get_state(self) -> dict:
        return deepcopy(self._state)


class Game:
    def __init__(self) -> None:
        self._level = 1
        self._score = 0
        self._inventory: list[str] = []

    def play(self, score: int, item: str | None = None) -> None:
        self._score += score
        if self._score >= self._level * 100:
            self._level += 1
        if item:
            self._inventory.append(item)

    def save(self) -> GameMemento:
        return GameMemento({
            "level": self._level,
            "score": self._score,
            "inventory": self._inventory,
        })

    def load(self, memento: GameMemento) -> None:
        state = memento.get_state()
        self._level = state["level"]
        self._score = state["score"]
        self._inventory = state["inventory"]

    def __repr__(self) -> str:
        return f"Game(level={self._level}, score={self._score}, inventory={self._inventory})"


def main() -> None:
    game = Game()
    game.play(120, "меч")
    print("После игры:", game)

    checkpoint = game.save()
    print("Сохранение создано.")

    game.play(50, "щит")
    print("После продолжения:", game)

    game.load(checkpoint)
    print("После загрузки:", game)


if __name__ == "__main__":
    main()
