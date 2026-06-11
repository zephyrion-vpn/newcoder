import random
import socket
import struct


def build_query(domain: str, qtype: int = 1) -> tuple[int, bytes]:
    transaction_id = random.randint(0, 0xFFFF)
    header = struct.pack(">HHHHHH", transaction_id, 0x0100, 1, 0, 0, 0)
    question = b"".join(
        struct.pack("B", len(part)) + part.encode("ascii") for part in domain.split(".")
    )
    question += b"\x00" + struct.pack(">HH", qtype, 1)
    return transaction_id, header + question


def parse_name(data: bytes, offset: int) -> tuple[str, int]:
    labels: list[str] = []
    jumped = False
    next_offset = offset
    while True:
        length = data[offset]
        if length & 0xC0 == 0xC0:
            pointer = struct.unpack(">H", data[offset : offset + 2])[0] & 0x3FFF
            if not jumped:
                next_offset = offset + 2
            offset = pointer
            jumped = True
            continue
        offset += 1
        if length == 0:
            break
        labels.append(data[offset : offset + length].decode("ascii"))
        offset += length
    return ".".join(labels), (next_offset if jumped else offset)


def resolve(domain: str, server: str = "8.8.8.8", timeout: float = 3.0) -> list[str]:
    transaction_id, query = build_query(domain)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(query, (server, 53))
        data, _ = sock.recvfrom(512)
    _, _, question_count, answer_count, _, _ = struct.unpack(">HHHHHH", data[:12])
    offset = 12
    for _ in range(question_count):
        _, offset = parse_name(data, offset)
        offset += 4
    addresses: list[str] = []
    for _ in range(answer_count):
        _, offset = parse_name(data, offset)
        rtype, _, _, rdlength = struct.unpack(">HHIH", data[offset : offset + 10])
        offset += 10
        rdata = data[offset : offset + rdlength]
        offset += rdlength
        if rtype == 1 and rdlength == 4:
            addresses.append(".".join(str(byte) for byte in rdata))
    return addresses


def main() -> None:
    domain = "example.com"
    try:
        addresses = resolve(domain)
    except (socket.timeout, OSError) as error:
        print(f"Нет доступа к DNS-серверу: {error}")
        return
    print(f"{domain} -> {addresses or 'записи не найдены'}")


if __name__ == "__main__":
    main()
