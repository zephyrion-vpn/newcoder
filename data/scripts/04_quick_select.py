import random


def quick_select_kth_largest(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("k вне диапазона.")
    arr = list(nums)
    target = len(arr) - k  # индекс k-го наибольшего в отсортированном по возрастанию
    left, right = 0, len(arr) - 1
    while True:
        pivot_index = _partition(arr, left, right)
        if pivot_index == target:
            return arr[pivot_index]
        if pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1


def _partition(arr: list[int], left: int, right: int) -> int:
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot = arr[right]
    store = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    arr[store], arr[right] = arr[right], arr[store]
    return store


def main() -> None:
    nums = [3, 2, 1, 5, 6, 4]
    for k in range(1, len(nums) + 1):
        result = quick_select_kth_largest(nums, k)
        expected = sorted(nums, reverse=True)[k - 1]
        print(f"{k}-й наибольший: {result} (ожидалось {expected}) -> {result == expected}")


if __name__ == "__main__":
    main()
