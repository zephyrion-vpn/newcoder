def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda pair: pair[0])
    merged: list[list[int]] = [list(ordered[0])]
    for start, end in ordered[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    return merged


def main() -> None:
    cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [2, 3]],
        [],
    ]
    for case in cases:
        print(f"{case} → {merge_intervals(case)}")


if __name__ == "__main__":
    main()
