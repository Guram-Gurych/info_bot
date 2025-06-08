from aiogram.fsm.state import State, StatesGroup


class SaveNoteFSM(StatesGroup):
    waiting_for_title = State()
    waiting_for_content = State()
