import random
from collections import Counter

ROLLS = 1000


def main() -> None:
    counts = Counter(random.randint(1, 6) + random.randint(1, 6) for _ in range(ROLLS))
    print(f"Статистика за {ROLLS} бросков:")
    for total in range(2, 13):
        count = counts[total]
        bar = "#" * (count * 50 // ROLLS)
        print(f"{total:>2}: {count:>4} {bar}")


if __name__ == "__main__":
    main()
