from functools import lru_cache

import aiohttp

from config.constants import API_URL, WEATHER_URL


@lru_cache(maxsize=128)
def get_cached_weather(city: str) -> tuple[float, float]:
    import asyncio
    return asyncio.run(fetch_coordinates(city))


async def fetch_coordinates(city: str) -> tuple[float, float]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL.format(city=city), timeout=5) as resp:
                data = await resp.json()
                results = data.get("results")
                if not results:
                    return None
                lat = results[0]["latitude"]
                lon = results[0]["longitude"]
                return lat, lon
    except Exception:
        return None


async def fetch_weather(city: str) -> str:
    coords = await fetch_coordinates(city)
    if coords is None:
        return "Город не найден или API недоступен"

    lat, lon = coords

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEATHER_URL.format(lat=lat, lon=lon), timeout=5) as resp:
                data = await resp.json()
                temp = data.get("current", {}).get("temperature_2m")
                if temp is not None:
                    return f"Погода сейчас в {city.title()} {temp}°C"
                return "Не удалось получить температуру"
    except Exception:
        return "Ошибка при получении погоды"
