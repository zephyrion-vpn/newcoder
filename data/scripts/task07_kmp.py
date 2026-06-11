def _prefix_function(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = lps[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        lps[i] = k
    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    if not pattern:
        raise ValueError("Подстрока не может быть пустой.")
    lps = _prefix_function(pattern)
    matches: list[int] = []
    k = 0
    for i, char in enumerate(text):
        while k and char != pattern[k]:
            k = lps[k - 1]
        if char == pattern[k]:
            k += 1
        if k == len(pattern):
            matches.append(i - k + 1)
            k = lps[k - 1]
    return matches


def main() -> None:
    text = "abracadabra abracadabra"
    pattern = "abra"
    print(f"Текст: {text!r}")
    print(f"Шаблон: {pattern!r}")
    print("Позиции:", kmp_search(text, pattern))


if __name__ == "__main__":
    main()
