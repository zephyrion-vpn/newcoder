import struct
from typing import Any

TYPE_NONE = 0
TYPE_BOOL = 1
TYPE_INT = 2
TYPE_FLOAT = 3
TYPE_STR = 4
TYPE_BYTES = 5
TYPE_LIST = 6
TYPE_DICT = 7


def serialize(obj: Any) -> bytes:
    if obj is None:
        return bytes([TYPE_NONE])
    if isinstance(obj, bool):
        return bytes([TYPE_BOOL, 1 if obj else 0])
    if isinstance(obj, int):
        return bytes([TYPE_INT]) + struct.pack("!q", obj)
    if isinstance(obj, float):
        return bytes([TYPE_FLOAT]) + struct.pack("!d", obj)
    if isinstance(obj, str):
        encoded = obj.encode("utf-8")
        return bytes([TYPE_STR]) + struct.pack("!I", len(encoded)) + encoded
    if isinstance(obj, bytes):
        return bytes([TYPE_BYTES]) + struct.pack("!I", len(obj)) + obj
    if isinstance(obj, list):
        out = bytes([TYPE_LIST]) + struct.pack("!I", len(obj))
        for item in obj:
            out += serialize(item)
        return out
    if isinstance(obj, dict):
        out = bytes([TYPE_DICT]) + struct.pack("!I", len(obj))
        for key, value in obj.items():
            out += serialize(key)
            out += serialize(value)
        return out
    raise TypeError(f"Неподдерживаемый тип: {type(obj)}")


def _deserialize(data: bytes, offset: int) -> tuple[Any, int]:
    tag = data[offset]
    offset += 1
    if tag == TYPE_NONE:
        return None, offset
    if tag == TYPE_BOOL:
        value = data[offset] == 1
        return value, offset + 1
    if tag == TYPE_INT:
        value = struct.unpack_from("!q", data, offset)[0]
        return value, offset + 8
    if tag == TYPE_FLOAT:
        value = struct.unpack_from("!d", data, offset)[0]
        return value, offset + 8
    if tag == TYPE_STR:
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        value = data[offset : offset + length].decode("utf-8")
        return value, offset + length
    if tag == TYPE_BYTES:
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        value = data[offset : offset + length]
        return value, offset + length
    if tag == TYPE_LIST:
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        items = []
        for _ in range(length):
            item, offset = _deserialize(data, offset)
            items.append(item)
        return items, offset
    if tag == TYPE_DICT:
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        result = {}
        for _ in range(length):
            key, offset = _deserialize(data, offset)
            value, offset = _deserialize(data, offset)
            result[key] = value
        return result, offset
    raise ValueError(f"Неизвестный тег: {tag}")


def deserialize(data: bytes) -> Any:
    value, _ = _deserialize(data, 0)
    return value


def main() -> None:
    original = {
        "name": "Серёга",
        "age": 30,
        "scores": [10, 20, 30.5],
        "active": True,
        "meta": {"nested": {"deep": [1, 2, {"x": None}]}},
        "blob": b"\x00\x01\x02",
    }
    encoded = serialize(original)
    decoded = deserialize(encoded)
    print(f"Размер бинарных данных: {len(encoded)} байт")
    print(f"Десериализовано: {decoded}")
    print(f"Совпадает с исходным: {decoded == original}")


if __name__ == "__main__":
    main()
