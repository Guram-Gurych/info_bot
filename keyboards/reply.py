from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="/joke"),
                KeyboardButton(text="/weather"),
            ],
            [
                KeyboardButton(text="/save"),
                KeyboardButton(text="/list"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
