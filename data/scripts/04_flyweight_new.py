class Color:
    _cache: dict[tuple[int, int, int], "Color"] = {}

    def __new__(cls, r: int, g: int, b: int) -> "Color":
        key = (r, g, b)
        if key in cls._cache:
            return cls._cache[key]
        instance = super().__new__(cls)
        cls._cache[key] = instance
        return instance

    def __init__(self, r: int, g: int, b: int) -> None:
        # __init__ вызывается каждый раз, поэтому защищаемся от повторной инициализации.
        if getattr(self, "_initialized", False):
            return
        self.r, self.g, self.b = r, g, b
        self._initialized = True

    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b})"


def main() -> None:
    red1 = Color(255, 0, 0)
    red2 = Color(255, 0, 0)
    blue = Color(0, 0, 255)
    print(f"red1 = {red1}, red2 = {red2}, blue = {blue}")
    print(f"red1 is red2: {red1 is red2}")
    print(f"red1 is blue: {red1 is blue}")
    print(f"Размер кэша: {len(Color._cache)}")


if __name__ == "__main__":
    main()
