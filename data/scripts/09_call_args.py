def total(*args: float) -> float:
    return sum(args)


if __name__ == "__main__":
    print(total(1, 2, 3))
    print(total(1, 2, 3, 4))
    print(total(1, 2, 3, 4, 5))
