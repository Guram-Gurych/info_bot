from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_joke_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ещё шутку", callback_data="more_jokes")]
        ]
    )
    return keyboard
