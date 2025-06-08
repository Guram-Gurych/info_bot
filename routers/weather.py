from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from services.weather_api import fetch_weather
from states.weather import WeatherStates

router = Router()


@router.message(F.text == "/weather")
async def cmd_weather(message: Message, state: FSMContext):
    await message.answer("Введите название города:")
    await state.set_state(WeatherStates.waiting_for_city)


@router.message(WeatherStates.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    city = message.text.strip()
    await message.answer("Получаю данные...")
    result = await fetch_weather(city)
    await message.answer(result)
    await state.clear()
