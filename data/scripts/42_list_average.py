def average(items: list[float]) -> float:
    return sum(items) / len(items) if items else 0.0


if __name__ == "__main__":
    print(average([2, 4, 6]))
