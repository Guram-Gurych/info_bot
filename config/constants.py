from pathlib import Path

JOKE_URL = "https://v2.jokeapi.dev/joke/Any?type=single"
API_URL = "https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
STORAGE_PATH = Path("storage/data.json")
DATABASE_URL = "sqlite:///storage/database.db"
