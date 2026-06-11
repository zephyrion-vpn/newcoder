import json
import sys
import urllib.error
import urllib.parse
import urllib.request

_GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def _get_json(url: str, params: dict[str, object]) -> dict:
    query = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{query}", timeout=10) as response:
        return json.load(response)


def current_temperature(city: str) -> tuple[str, float]:
    geo = _get_json(_GEOCODE_URL, {"name": city, "count": 1, "language": "ru"})
    results = geo.get("results")
    if not results:
        raise ValueError(f"Город не найден: {city}")
    location = results[0]
    forecast = _get_json(
        _FORECAST_URL,
        {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m",
        },
    )
    return location["name"], forecast["current"]["temperature_2m"]


def main() -> None:
    city = " ".join(sys.argv[1:]).strip() or "Moscow"
    try:
        name, temperature = current_temperature(city)
    except (urllib.error.URLError, ValueError, KeyError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"{name}: {temperature}°C")


if __name__ == "__main__":
    main()
