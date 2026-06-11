MILES_PER_KM = 0.621371


def km_to_miles(kilometers: float) -> float:
    return kilometers * MILES_PER_KM


def main() -> None:
    for km in (1, 5, 10, 42.195):
        print(f"{km} км = {km_to_miles(km):.3f} миль")


if __name__ == "__main__":
    main()
