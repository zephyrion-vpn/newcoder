from __future__ import annotations


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} (зп: {self.salary})"


class Manager(Employee):
    def __init__(self, name: str, salary: float, subordinates: list[Employee] | None = None) -> None:
        super().__init__(name, salary)
        self.subordinates: list[Employee] = list(subordinates) if subordinates else []

    def add_subordinate(self, employee: Employee) -> None:
        self.subordinates.append(employee)

    def __str__(self) -> str:
        names = ", ".join(e.name for e in self.subordinates) or "нет"
        return f"{self.name} (менеджер, подчинённые: {names})"


def main() -> None:
    dev = Employee("Анна", 100000)
    qa = Employee("Борис", 90000)
    manager = Manager("Виктор", 150000, [dev])
    manager.add_subordinate(qa)
    print(manager)
    print(f"Число подчинённых: {len(manager.subordinates)}")


if __name__ == "__main__":
    main()
