from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from keyboards.inline import get_joke_keyboard
from keyboards.reply import get_main_keyboard
from services.api_client import get_joke

router = Router()


@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Привет! Я GuramBot. Отправь /help, чтобы узнать команды.")


@router.message(F.text == "/help")
async def help_cmd(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — запустить бота\n"
        "/help — справка\n"
        "/joke — получить случайную шутку\n"
        "/weather — прогноз погоды\n"
        "/save — сохранить заметку\n"
        "/list — список заметок\n"
        "/delete — удалить заметку",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "/joke")
async def joke_cmd(message: Message):
    joke_text = await get_joke()
    await message.answer(joke_text, reply_markup=get_joke_keyboard())


@router.callback_query(F.data == "more_jokes")
async def joke_callback(callback: CallbackQuery):
    joke_text = await get_joke()
    await callback.message.answer(joke_text, reply_markup=get_joke_keyboard())
    await callback.answer()
