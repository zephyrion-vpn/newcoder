class ConstantHashSet(frozenset):
    # Переопределяем __hash__: все экземпляры попадают в одну корзину (демонстрация коллизий).
    def __hash__(self) -> int:
        return 42


class SumHashSet(frozenset):
    # Кастомное хеширование: хеш зависит от суммы элементов.
    def __hash__(self) -> int:
        return sum(hash(item) for item in self)


def main() -> None:
    a = ConstantHashSet([1, 2, 3])
    b = ConstantHashSet([4, 5, 6])
    print(f"hash(a) = {hash(a)}, hash(b) = {hash(b)} — коллизия: {hash(a) == hash(b)}")
    print(f"a == b: {a == b} (равенство по содержимому сохраняется)")

    # Оба ключа работают в dict несмотря на одинаковый хеш (разрешение коллизий).
    mapping = {a: "first", b: "second"}
    print(f"Различных ключей в dict: {len(mapping)}")

    s = SumHashSet([10, 20, 30])
    print(f"SumHashSet hash = {hash(s)} (сумма 60)")


if __name__ == "__main__":
    main()
