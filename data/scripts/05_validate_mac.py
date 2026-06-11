import re

MAC_PATTERN = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")


def is_valid_mac(address: str) -> bool:
    return MAC_PATTERN.fullmatch(address.strip()) is not None


def main() -> None:
    for address in ["01:23:45:67:89:AB", "FF:FF:FF:FF:FF:FF", "01:23:45:67:89", "GG:23:45:67:89:AB", "0123.4567.89AB"]:
        print(f"{address}: {is_valid_mac(address)}")


if __name__ == "__main__":
    main()
