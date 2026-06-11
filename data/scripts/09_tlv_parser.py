import struct
from dataclasses import dataclass


@dataclass
class TLV:
    type: int
    value: bytes

    def encode(self) -> bytes:
        # Type: 1 байт, Length: 2 байта (big-endian), Value: Length байт.
        return struct.pack("!BH", self.type, len(self.value)) + self.value


def encode_all(items: list[TLV]) -> bytes:
    return b"".join(item.encode() for item in items)


def parse(data: bytes) -> list[TLV]:
    items: list[TLV] = []
    offset = 0
    while offset < len(data):
        if offset + 3 > len(data):
            raise ValueError("Неполный заголовок TLV.")
        tlv_type, length = struct.unpack("!BH", data[offset : offset + 3])
        offset += 3
        if offset + length > len(data):
            raise ValueError("Длина значения выходит за границы буфера.")
        value = data[offset : offset + length]
        offset += length
        items.append(TLV(tlv_type, value))
    return items


def main() -> None:
    original = [
        TLV(1, b"username"),
        TLV(2, b"\x00\x01\x02\x03"),
        TLV(3, "привет".encode("utf-8")),
    ]
    encoded = encode_all(original)
    print(f"Закодировано байт: {len(encoded)}")
    print(f"Hex: {encoded.hex()}")

    decoded = parse(encoded)
    print("\nРазобрано:")
    for item in decoded:
        print(f"   type={item.type}, len={len(item.value)}, value={item.value!r}")

    print(f"\nСовпадает с исходным: {decoded == original}")


if __name__ == "__main__":
    main()
