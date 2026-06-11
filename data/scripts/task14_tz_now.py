from datetime import datetime


def now_in_zone(tz_name: str) -> datetime:
    try:
        from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

        try:
            return datetime.now(ZoneInfo(tz_name))
        except ZoneInfoNotFoundError:
            pass
    except ImportError:
        pass
    import pytz

    return datetime.now(pytz.timezone(tz_name))


def main() -> None:
    for tz_name in ("Europe/Moscow", "America/New_York", "Asia/Tokyo"):
        moment = now_in_zone(tz_name)
        print(f"{tz_name}: {moment:%Y-%m-%d %H:%M:%S %Z}")


if __name__ == "__main__":
    main()
