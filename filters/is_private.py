from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == "private"
