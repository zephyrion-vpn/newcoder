import socket
import struct
import sys


def parse_ip_header(packet: bytes) -> tuple[int, int, str, str]:
    version_ihl = packet[0]
    ihl = (version_ihl & 0x0F) * 4
    protocol = packet[9]
    source = socket.inet_ntoa(packet[12:16])
    destination = socket.inet_ntoa(packet[16:20])
    return ihl, protocol, source, destination


def parse_tcp_header(segment: bytes) -> tuple[int, int, int, int, int]:
    source_port, destination_port, sequence, acknowledgment, offset_byte = struct.unpack(
        ">HHIIB", segment[:13]
    )
    data_offset = (offset_byte >> 4) * 4
    return source_port, destination_port, sequence, acknowledgment, data_offset


def sniff(count: int = 5, timeout: float = 5.0) -> None:
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    sniffer.settimeout(timeout)
    captured = 0
    while captured < count:
        try:
            packet, _ = sniffer.recvfrom(65535)
        except socket.timeout:
            print("Таймаут ожидания пакетов.")
            break
        ihl, protocol, source, destination = parse_ip_header(packet)
        if protocol != socket.IPPROTO_TCP:
            continue
        source_port, destination_port, sequence, _, _ = parse_tcp_header(packet[ihl:])
        print(f"{source}:{source_port} -> {destination}:{destination_port} seq={sequence}")
        captured += 1
    sniffer.close()


def main() -> None:
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    try:
        sniff(count=count)
    except PermissionError:
        print("Для raw socket нужны права root (запустите через sudo).")
    except OSError as error:
        print(f"Ошибка сети: {error}")


if __name__ == "__main__":
    main()
