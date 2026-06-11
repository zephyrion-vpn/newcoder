class Amplifier:
    def on(self) -> None:
        print("Усилитель включён")

    def set_volume(self, level: int) -> None:
        print(f"Громкость: {level}")

    def off(self) -> None:
        print("Усилитель выключен")


class Projector:
    def on(self) -> None:
        print("Проектор включён")

    def wide_screen(self) -> None:
        print("Режим 16:9")

    def off(self) -> None:
        print("Проектор выключен")


class Screen:
    def down(self) -> None:
        print("Экран опущен")

    def up(self) -> None:
        print("Экран поднят")


class HomeTheaterFacade:
    def __init__(self, amplifier: Amplifier, projector: Projector, screen: Screen) -> None:
        self._amplifier = amplifier
        self._projector = projector
        self._screen = screen

    def watch_movie(self, title: str) -> None:
        print(f"Готовим просмотр: {title}")
        self._screen.down()
        self._projector.on()
        self._projector.wide_screen()
        self._amplifier.on()
        self._amplifier.set_volume(8)
        print("Приятного просмотра!")

    def end_movie(self) -> None:
        print("Завершаем просмотр")
        self._amplifier.off()
        self._projector.off()
        self._screen.up()


def main() -> None:
    theater = HomeTheaterFacade(Amplifier(), Projector(), Screen())
    theater.watch_movie("Интерстеллар")
    print("-" * 20)
    theater.end_movie()


if __name__ == "__main__":
    main()
