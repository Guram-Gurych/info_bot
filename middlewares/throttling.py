import asyncio
from typing import Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, delay: float = 1.5):
        self.delay = delay
        self._users: Dict[int, bool] = {}

    async def __call__(
        self,
        handler: Callable[[Message, dict], Awaitable],
        event: Message,
        data: dict
    ) -> None:
        user_id = event.from_user.id
        if self._users.get(user_id):
            await event.answer("Подожди немного перед следующим сообщением.")
            return
        self._users[user_id] = True
        try:
            await handler(event, data)
        finally:
            await asyncio.sleep(self.delay)
            self._users.pop(user_id, None)
