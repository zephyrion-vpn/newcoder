from typing import Optional


def max_sum_subarray(nums: list[int], k: int) -> Optional[int]:
    if k <= 0 or k > len(nums):
        return None
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best


def main() -> None:
    cases = [
        ([2, 1, 5, 1, 3, 2], 3),
        ([2, 3, 4, 1, 5], 2),
        ([1, 2, 3], 5),
        ([-1, -2, -3, -4], 2),
    ]
    for nums, k in cases:
        print(f"nums={nums}, k={k} → {max_sum_subarray(nums, k)}")


if __name__ == "__main__":
    main()
