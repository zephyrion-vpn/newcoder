def longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s
    start, end = 0, 0

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start : end + 1]


def manacher(s: str) -> str:
    if not s:
        return ""
    t = "#" + "#".join(s) + "#"
    n = len(t)
    radius = [0] * n
    center = right = 0
    for i in range(n):
        if i < right:
            radius[i] = min(right - i, radius[2 * center - i])
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < n and t[i - radius[i] - 1] == t[i + radius[i] + 1]:
            radius[i] += 1
        if i + radius[i] > right:
            center, right = i, i + radius[i]
    max_len, center_index = max((r, i) for i, r in enumerate(radius))
    start = (center_index - max_len) // 2
    return s[start : start + max_len]


def main() -> None:
    for text in ("babad", "cbbd", "forgeeksskeegfor", "a", ""):
        print(f"{text!r}: center={longest_palindrome(text)!r}, manacher={manacher(text)!r}")


if __name__ == "__main__":
    main()
