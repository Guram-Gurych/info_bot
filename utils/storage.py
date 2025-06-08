import json

from config.constants import STORAGE_PATH


def _load_data() -> dict:
    if not STORAGE_PATH.exists():
        return {}
    with open(STORAGE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_data(data: dict) -> None:
    with open(STORAGE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def add_note(user_id: int, title: str, content: str) -> None:
    data = _load_data()
    user_notes = data.get(str(user_id), [])
    user_notes.append({"title": title, "content": content})
    data[str(user_id)] = user_notes
    _save_data(data)


def get_notes(user_id: int) -> list:
    data = _load_data()
    return data.get(str(user_id), [])


def delete_note(user_id: int, index: int) -> bool:
    data = _load_data()
    notes = data.get(str(user_id), [])
    if 0 <= index < len(notes):
        notes.pop(index)
        data[str(user_id)] = notes
        _save_data(data)
        return True
    return False


def get_statistics() -> tuple[int, int]:
    data = _load_data()
    total_users = len(data)
    total_notes = sum(len(notes) for notes in data.values())
    return total_users, total_notes
