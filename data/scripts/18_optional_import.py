import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("optional")

try:
    import numpy as np  # type: ignore
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    logger.warning("numpy не установлен, использую резервный алгоритм на чистом Python.")


def dot_product(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("векторы разной длины")
    if HAS_NUMPY:
        return float(np.dot(np.array(a), np.array(b)))
    return float(sum(x * y for x, y in zip(a, b)))


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("пустой список")
    if HAS_NUMPY:
        return float(np.mean(np.array(values)))
    return sum(values) / len(values)


def main() -> None:
    print(f"numpy доступен: {HAS_NUMPY}")
    a = [1.0, 2.0, 3.0]
    b = [4.0, 5.0, 6.0]
    print(f"Скалярное произведение: {dot_product(a, b)} (ожидается 32.0)")
    print(f"Среднее [1..3]: {mean(a)} (ожидается 2.0)")


if __name__ == "__main__":
    main()
