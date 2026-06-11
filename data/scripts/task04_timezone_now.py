from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def now_in_timezone(timezone: str) -> datetime:
    try:
        return datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError as error:
        raise ValueError(f"Неизвестная временная зона: {timezone}") from error


def main() -> None:
    timezone = "Europe/Moscow"
    print(f"{timezone}: {now_in_timezone(timezone).isoformat()}")


if __name__ == "__main__":
    main()
