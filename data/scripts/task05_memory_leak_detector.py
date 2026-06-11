import gc
from collections import Counter


class Session:
    def __init__(self, session_id: int) -> None:
        self.session_id = session_id
        self.payload = [0] * 16


_leaked: list[Session] = []


def type_counts() -> Counter[str]:
    counter: Counter[str] = Counter()
    for obj in gc.get_objects():
        counter[type(obj).__name__] += 1
    return counter


def leaky_iteration(batch: int) -> None:
    for index in range(batch):
        _leaked.append(Session(index))


def detect_leaks(iterations: int = 5, batch: int = 500) -> None:
    gc.collect()
    baseline = type_counts()
    for step in range(1, iterations + 1):
        leaky_iteration(batch)
        gc.collect()
        current = type_counts()
        growth = {
            name: current[name] - baseline[name]
            for name in current
            if current[name] - baseline[name] > 0
        }
        top = sorted(growth.items(), key=lambda item: item[1], reverse=True)[:3]
        report = ", ".join(f"{name}: +{delta}" for name, delta in top)
        print(f"итерация {step}: {report}")


def main() -> None:
    detect_leaks()
    print("Подозрение на утечку: Session растёт линейно между итерациями")


if __name__ == "__main__":
    main()
