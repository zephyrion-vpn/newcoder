import json
from typing import Any, Iterator


def stream_with_ijson(path: str) -> Iterator[Any]:
    import ijson

    with open(path, "rb") as handle:
        yield from ijson.items(handle, "item")


def stream_fallback(path: str, chunk_size: int = 65536) -> Iterator[Any]:
    depth = 0
    in_string = False
    escape = False
    started = False
    buffer: list[str] = []
    with open(path, encoding="utf-8") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            for char in chunk:
                if not started:
                    if char == "[":
                        started = True
                    continue
                if in_string:
                    buffer.append(char)
                    if escape:
                        escape = False
                    elif char == "\\":
                        escape = True
                    elif char == '"':
                        in_string = False
                    continue
                if char == '"':
                    in_string = True
                    buffer.append(char)
                elif char == "{":
                    depth += 1
                    buffer.append(char)
                elif char == "}":
                    depth -= 1
                    buffer.append(char)
                    if depth == 0:
                        yield json.loads("".join(buffer))
                        buffer.clear()
                elif depth > 0:
                    buffer.append(char)


def stream_objects(path: str) -> Iterator[Any]:
    try:
        import ijson  # noqa: F401
    except ImportError:
        print("[fallback] ijson не найден, использую ручной потоковый парсер")
        yield from stream_fallback(path)
    else:
        print("[ijson] использую ijson")
        yield from stream_with_ijson(path)


def main() -> None:
    import tempfile

    path = tempfile.mktemp(suffix=".json")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("[\n")
        for i in range(5):
            handle.write(json.dumps({"id": i, "name": f"объект-{i}"}, ensure_ascii=False))
            handle.write(",\n" if i < 4 else "\n")
        handle.write("]\n")
    for obj in stream_objects(path):
        print("получен:", obj)


if __name__ == "__main__":
    main()
