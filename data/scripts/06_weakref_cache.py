import gc
import weakref


class Resource:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Resource({self.name!r})"


class WeakCache:
    def __init__(self) -> None:
        self._cache: weakref.WeakValueDictionary[str, Resource] = weakref.WeakValueDictionary()

    def get(self, name: str) -> Resource | None:
        return self._cache.get(name)

    def put(self, name: str, resource: Resource) -> None:
        self._cache[name] = resource

    def __len__(self) -> int:
        return len(self._cache)


def main() -> None:
    cache = WeakCache()
    strong = Resource("alpha")
    cache.put("alpha", strong)
    cache.put("beta", Resource("beta"))  # нет сильной ссылки

    gc.collect()
    print(f"После сборки: alpha={cache.get('alpha')}, beta={cache.get('beta')}")
    print(f"Размер кэша: {len(cache)} (beta удалён, т.к. нет сильных ссылок)")

    del strong
    gc.collect()
    print(f"После del strong: alpha={cache.get('alpha')}, размер={len(cache)}")


if __name__ == "__main__":
    main()
