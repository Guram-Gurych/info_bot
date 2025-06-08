from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config.constants import DATABASE_URL
from storage.models import Base, Note

engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)


def add_note(user_id: int, content: str):
    with Session(engine) as session:
        note = Note(user_id=user_id, content=content)
        session.add(note)
        session.commit()


def get_notes(user_id: int) -> list[Note]:
    with Session(engine) as session:
        return session.scalars(
            select(Note).where(Note.user_id == user_id)
        ).all()


def delete_note(user_id: int, note_index: int) -> bool:
    with Session(engine) as session:
        notes = session.scalars(
            select(Note).where(Note.user_id == user_id)
        ).all()

        if 0 <= note_index < len(notes):
            session.delete(notes[note_index])
            session.commit()
            return True
        return False


def count_total_notes() -> int:
    with Session(engine) as session:
        return session.query(Note).count()
