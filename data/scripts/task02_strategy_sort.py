from abc import ABC, abstractmethod


class SortStrategy(ABC):
    name: str

    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        ...


class InsertionSort(SortStrategy):
    name = "insertion"

    def sort(self, data: list[int]) -> list[int]:
        result = list(data)
        for i in range(1, len(result)):
            key = result[i]
            j = i - 1
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = key
        return result


class MergeSort(SortStrategy):
    name = "merge"

    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return list(data)
        middle = len(data) // 2
        left = self.sort(data[:middle])
        right = self.sort(data[middle:])
        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        merged: list[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


class TimSortStrategy(SortStrategy):
    name = "timsort"

    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)


def choose_strategy(size: int) -> SortStrategy:
    if size <= 16:
        return InsertionSort()
    if size <= 1000:
        return MergeSort()
    return TimSortStrategy()


def main() -> None:
    for size in (10, 500, 5000):
        data = [(size - i) % 97 for i in range(size)]
        strategy = choose_strategy(size)
        ordered = strategy.sort(data)
        print(f"размер {size}: стратегия {strategy.name}, отсортировано: {ordered == sorted(data)}")


if __name__ == "__main__":
    main()
