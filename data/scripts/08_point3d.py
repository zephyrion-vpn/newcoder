from __future__ import annotations

import math

EPSILON = 1e-6


class Point3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: "Point3D") -> float:
        return math.dist((self.x, self.y, self.z), (other.x, other.y, other.z))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            return NotImplemented
        return self.distance_to(other) < EPSILON

    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"


def main() -> None:
    a = Point3D(1.0, 2.0, 3.0)
    b = Point3D(1.0, 2.0, 3.0 + 1e-9)
    c = Point3D(1.0, 2.0, 4.0)
    print(a == b)
    print(a == c)


if __name__ == "__main__":
    main()
