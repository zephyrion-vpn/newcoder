import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

try:
    import numpy as np  # type: ignore
    HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore
    HAS_NUMPY = False
    logger.warning("Модуль numpy не найден, использую резервный алгоритм.")


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Пустой список.")
    if HAS_NUMPY:
        return float(np.mean(values))
    return sum(values) / len(values)


def main() -> None:
    print(f"numpy доступен: {HAS_NUMPY}")
    print(f"Среднее: {mean([1, 2, 3, 4])}")


if __name__ == "__main__":
    main()
