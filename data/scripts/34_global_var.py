counter = 0


def increment() -> None:
    global counter
    counter += 1


if __name__ == "__main__":
    increment()
    print(counter)
