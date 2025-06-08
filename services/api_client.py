import aiohttp

from config.constants import JOKE_URL


async def get_joke() -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(JOKE_URL, timeout=5) as response:
                data = await response.json()
                return data.get("joke", "Не удалось получить шутку")
    except Exception:
        return "Ошибка при получении шутки"
