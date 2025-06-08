import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config.settings import settings
from filters.is_private import IsPrivate
from middlewares.throttling import ThrottlingMiddleware
from routers import (admin_router, commands_router, fallback_router,
                     storage_router, weather_router)
from utils.logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=MemoryStorage())  

    dp.message.middleware(ThrottlingMiddleware(delay=1.5))
    dp.message.filter(IsPrivate())

    dp.include_router(commands_router)
    dp.include_router(weather_router)
    dp.include_router(storage_router)
    dp.include_router(admin_router)
    dp.include_router(fallback_router)

    logger.info("Bot is starting polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as err:
        logger.warning(f"Bot stopped with error: {err}")
