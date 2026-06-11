import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("weather")

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10


def _get_json(url: str, params: dict[str, str]) -> Optional[dict]:
    query = urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(f"{url}?{query}", timeout=TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        logger.warning("Сеть недоступна: %s", error)
        return None


def get_temperature(city: str) -> Optional[float]:
    geo = _get_json(GEOCODE_URL, {"name": city, "count": "1", "language": "ru"})
    if not geo or not geo.get("results"):
        logger.warning("Город %r не найден или нет сети.", city)
        return None
    place = geo["results"][0]
    forecast = _get_json(FORECAST_URL, {
        "latitude": str(place["latitude"]),
        "longitude": str(place["longitude"]),
        "current_weather": "true",
    })
    if not forecast or "current_weather" not in forecast:
        return None
    return float(forecast["current_weather"]["temperature"])


def main() -> None:
    city = "Москва"
    print(f"Запрашиваю погоду для города: {city}")
    temperature = get_temperature(city)
    if temperature is None:
        print("Не удалось получить температуру (нет сети или API недоступен).")
    else:
        print(f"Температура в {city}: {temperature} °C")


if __name__ == "__main__":
    main()
