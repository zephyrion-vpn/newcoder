from math import hypot


def sort_by_distance(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    return sorted(points, key=lambda point: hypot(point[0], point[1]))


def main() -> None:
    points = [(3, 4), (1, 1), (0, 2), (5, 0), (-1, -1)]
    for point in sort_by_distance(points):
        print(point, round(hypot(point[0], point[1]), 3))


if __name__ == "__main__":
    main()
