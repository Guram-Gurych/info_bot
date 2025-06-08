from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.save import SaveNoteFSM
from storage.db import add_note, delete_note, get_notes

router = Router()


@router.message(F.text == "/save")
async def start_save(message: Message, state: FSMContext):
    await message.answer("Введите название заметки:")
    await state.set_state(SaveNoteFSM.waiting_for_title)


@router.message(SaveNoteFSM.waiting_for_title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text.strip())
    await message.answer("Теперь введите текст заметки:")
    await state.set_state(SaveNoteFSM.waiting_for_content)


@router.message(SaveNoteFSM.waiting_for_content)
async def get_content(message: Message, state: FSMContext):
    data = await state.get_data()
    title = data["title"]
    content = message.text.strip()

    add_note(user_id=message.from_user.id, content=f"{title}: {content}")
    await message.answer("Заметка сохранена.")
    await state.clear()


@router.message(F.text == "/list")
async def cmd_list(message: types.Message):
    notes = get_notes(message.from_user.id)
    if notes:
        text = "\n".join([f"{i+1}. {note.content}" for i, note in enumerate(notes)])
    else:
        text = "У вас пока нет заметок."
    await message.answer(text)


@router.message(F.text.startswith("/delete"))
async def cmd_delete(message: types.Message):
    try:
        index = int(message.text.split()[1]) - 1
    except (IndexError, ValueError):
        await message.answer(
            "Укажи номер заметки после команды `/delete <номер>`",
            parse_mode="Markdown",
        )
        return

    if delete_note(message.from_user.id, index):
        await message.answer("Заметка удалена.")
    else:
        await message.answer("Неверный номер заметки.")
