def describe(name: str, age: int = 18) -> str:
    return f"{name} is {age}"


if __name__ == "__main__":
    print(describe("Alex"))
