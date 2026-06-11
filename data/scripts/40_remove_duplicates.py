def unique(items: list[int]) -> list[int]:
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(unique([1, 2, 2, 3, 3, 3]))
