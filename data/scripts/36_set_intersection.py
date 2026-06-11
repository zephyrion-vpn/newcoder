def main() -> None:
    first = {1, 2, 3, 4}
    second = {3, 4, 5, 6}
    common = first & second
    print(f"Первое множество: {first}")
    print(f"Второе множество: {second}")
    if common:
        print(f"Общие элементы: {common}")
    else:
        print("Общих элементов нет.")


if __name__ == "__main__":
    main()
