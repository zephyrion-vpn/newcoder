MENU = """
1. Показать задачи
2. Добавить задачу
3. Удалить задачу
4. Выход
"""


def show_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("Список пуст.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks: list[str]) -> None:
    task = input("Текст задачи: ").strip()
    if task:
        tasks.append(task)
        print("Добавлено.")
    else:
        print("Пустая задача не добавлена.")


def remove_task(tasks: list[str]) -> None:
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Номер задачи для удаления: ").strip())
    except ValueError:
        print("Нужен номер задачи.")
        return
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Удалено: {removed}")
    else:
        print("Нет задачи с таким номером.")


def main() -> None:
    tasks: list[str] = []
    actions = {"1": lambda: show_tasks(tasks), "2": lambda: add_task(tasks), "3": lambda: remove_task(tasks)}
    while True:
        print(MENU)
        choice = input("Выбор: ").strip()
        if choice == "4":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
