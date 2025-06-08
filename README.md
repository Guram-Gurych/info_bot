
# Info Bot

InfoSphere — Telegram-бот, предоставляющий краткую и полезную информацию по запросу пользователя: от случайных фактов и шуток до погоды. Подходит для быстрой справки, хранения заметок и получения развлекательного контента.

---

## Авторы проекта

| Имя               | ИСУ     | Обязанности                                                                 |
|------------------|---------|------------------------------------------------------------------------------|
| **Кирилл Бледных** | 465230 | Архитектура проекта, настройка `.env` и логирования, <br> API-клиенты, хранилище, FSM и middleware |
| **Максим Серов**  | 467436 | Команды бота, обработка запросов, <br> кастомные фильтры, клавиатуры, админ-панель, README |

---

## Возможности

| Категория | Команды и описание                              |
|----------|-------------------------------------------------|
| Общие    | `/start`, `/help`                               |
| Инфо-контент | `/joke` — случайная шутка                       |
| Погода   | `/weather <город>` — текущая погода             |
| Заметки | `/save <текст>` — сохранить заметку             |
|          | `/list` — показать все заметки                  |
|          | `/delete <номер>` — удалить заметку             |
| Админ  | `/stats` — число пользователей и заметок        |

---

## Используемые технологии

- Python 3.11
- Aiogram 3
- `.env` для защиты токенов
- Логирование в файл
- FSM
- Middleware
- Кастомные фильтры (`IsAdmin`, `IsPrivate`)
- SQL для хранения данных

---

## Структура проекта

```
├── bot.log
├── bot.py
├── config
│   ├── constants.py
│   └── settings.py
├── filters
│   ├── is_admin.py
│   └── is_private.py
├── keyboards
│   ├── inline.py
│   └── reply.py
├── middlewares
│   └── throttling.py
├── requirements.txt
├── routers
│   ├── admin.py
│   ├── commands.py
│   ├── fallback.py
│   ├── storage_cmds.py
│   └── weather.py
├── services
│   ├── api_client.py
│   └── weather_api.py
├── states
│   ├── save.py
│   └── weather.py
├── storage
│   └── data.json
└── utils
    ├── logger.py
    └── storage.py
````

---

## Запуск проекта

```bash
git clone git@github.com:Guram-Gurych/info_bot.git
cd info_bot

python -m venv venv
source venv\Scripts\activate

pip install -r requirements.txt

python bot.py
```

