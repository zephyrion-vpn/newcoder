from typing import Any, Callable


def compose(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def composed(x: Any) -> Any:
        return f(g(x))
    return composed


def main() -> None:
    increment = lambda x: x + 1
    double = lambda x: x * 2
    inc_then_double = compose(double, increment)
    print(inc_then_double(5))
    str_then_upper = compose(str.upper, str)
    print(str_then_upper(123))


if __name__ == "__main__":
    main()
