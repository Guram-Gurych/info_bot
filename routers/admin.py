from aiogram import Router, types

from config.settings import settings
from filters.is_admin import IsAdmin
from storage.db import count_total_notes

router = Router()

@router.message(IsAdmin(admin_ids=settings.admin_ids))
async def cmd_stats(message: types.Message):
    total = count_total_notes()
    await message.answer(f"Всего заметок в системе: {total}")
