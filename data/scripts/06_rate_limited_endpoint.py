import time
from collections import defaultdict, deque


class RateLimiter:
    def __init__(self, max_requests: int = 10, window_seconds: float = 60.0) -> None:
        self.max_requests = max_requests
        self.window = window_seconds
        self._hits: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, ip: str, now: float | None = None) -> bool:
        current = time.monotonic() if now is None else now
        hits = self._hits[ip]
        while hits and current - hits[0] >= self.window:
            hits.popleft()
        if len(hits) >= self.max_requests:
            return False
        hits.append(current)
        return True


def main() -> None:
    limiter = RateLimiter(max_requests=10, window_seconds=60.0)
    ip = "192.168.0.1"
    allowed = 0
    blocked = 0
    base = 1000.0
    for i in range(15):
        if limiter.allow(ip, now=base + i * 0.1):
            allowed += 1
        else:
            blocked += 1
    print(f"IP {ip}: разрешено {allowed}, заблокировано {blocked} (лимит 10/мин)")

    # Через минуту окно очищается.
    later = limiter.allow(ip, now=base + 61)
    print(f"Спустя 61 сек разрешён: {later}")

    other = limiter.allow("10.0.0.5", now=base)
    print(f"Другой IP не затронут: {other}")


if __name__ == "__main__":
    main()
