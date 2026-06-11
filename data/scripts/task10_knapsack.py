from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    weight: int
    value: int


def knapsack(items: list[Item], capacity: int) -> tuple[int, list[Item]]:
    if capacity < 0:
        raise ValueError("Вместимость не может быть отрицательной.")
    if any(item.weight < 0 for item in items):
        raise ValueError("Вес предмета не может быть отрицательным.")

    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if item.weight <= w:
                candidate = dp[i - 1][w - item.weight] + item.value
                if candidate > dp[i][w]:
                    dp[i][w] = candidate

    chosen: list[Item] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(items[i - 1])
            w -= items[i - 1].weight
    chosen.reverse()
    return dp[n][capacity], chosen


def main() -> None:
    items = [
        Item("ноутбук", weight=3, value=2000),
        Item("камера", weight=1, value=1500),
        Item("книга", weight=2, value=300),
        Item("палатка", weight=4, value=1000),
    ]
    best_value, picked = knapsack(items, capacity=5)
    print("Максимальная ценность:", best_value)
    print("Взятые предметы:", [item.name for item in picked])


if __name__ == "__main__":
    main()
