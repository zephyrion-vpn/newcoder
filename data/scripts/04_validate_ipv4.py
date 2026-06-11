import re

OCTET = r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
IPV4_PATTERN = re.compile(rf"^{OCTET}\.{OCTET}\.{OCTET}\.{OCTET}$")


def is_valid_ipv4(address: str) -> bool:
    return IPV4_PATTERN.fullmatch(address.strip()) is not None


def main() -> None:
    for address in ["192.168.0.1", "255.255.255.255", "0.0.0.0", "256.1.1.1", "1.2.3", "01.2.3.4"]:
        print(f"{address}: {is_valid_ipv4(address)}")


if __name__ == "__main__":
    main()
