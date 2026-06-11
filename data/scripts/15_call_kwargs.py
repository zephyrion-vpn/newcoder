def describe(**kwargs: object) -> str:
    return ", ".join(f"{key}={value}" for key, value in kwargs.items())


if __name__ == "__main__":
    print(describe(name="Alex", age=20))
