from enum import Enum


class Planet:
    def __init__(self, mass: float, radius: float) -> None:
        self.mass = mass
        self.radius = radius

    @property
    def gravity(self) -> float:
        G = 6.67430e-11
        return G * self.mass / (self.radius ** 2)

    def __repr__(self) -> str:
        return f"Planet(mass={self.mass:.3e}, radius={self.radius:.3e})"


class SolarSystem(Enum):
    EARTH = Planet(5.976e24, 6.37814e6)
    MARS = Planet(6.421e23, 3.3972e6)
    JUPITER = Planet(1.9e27, 7.1492e7)

    @property
    def gravity(self) -> float:
        return self.value.gravity

    def weight(self, mass_kg: float) -> float:
        return mass_kg * self.gravity


def main() -> None:
    for planet in SolarSystem:
        print(f"{planet.name:8} g = {planet.gravity:6.2f} м/с², вес 75кг = {planet.weight(75):8.1f} Н")
    print(f"\nSolarSystem.EARTH — экземпляр Enum: {isinstance(SolarSystem.EARTH, SolarSystem)}")
    print(f"Значение — экземпляр Planet: {isinstance(SolarSystem.EARTH.value, Planet)}")


if __name__ == "__main__":
    main()
