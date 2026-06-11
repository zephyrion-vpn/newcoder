def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    cubes = list(map(lambda x: x ** 3, numbers))
    print(cubes)


if __name__ == "__main__":
    main()
