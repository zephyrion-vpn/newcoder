def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    merged: list[int] = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged


def main() -> None:
    print(merge_sorted([1, 3, 5, 7], [2, 4, 6, 8]))
    print(merge_sorted([1, 2, 3], []))
    print(merge_sorted([], [4, 5]))
    print(merge_sorted([1, 1, 2], [1, 3]))


if __name__ == "__main__":
    main()
