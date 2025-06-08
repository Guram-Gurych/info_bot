import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def parse_admin_ids(raw_ids: str) -> list[int]:
    return [int(i) for i in raw_ids.split(",") if i.strip().isdigit()]


@dataclass
class Settings:
    bot_token: str
    admin_ids: list[int]


settings = Settings(
    bot_token=os.getenv("BOT_TOKEN"),
    admin_ids=parse_admin_ids(os.getenv("ADMINS", "")),
)
