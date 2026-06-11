def main() -> None:
    matrix = [[1, 2, 3], [4, 5, 6]]
    target = 5
    position = None
    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if value == target:
                position = (row_index, column_index)
                break
        if position is not None:
            break
    print(position)


if __name__ == "__main__":
    main()
