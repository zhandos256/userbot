# Telegram Bot Template на Aiogram 3.18.0

Современный шаблон для разработки Telegram-ботов на базе Aiogram 3.18.0. Включает в себя все необходимые компоненты для создания масштабируемых и поддерживаемых ботов.

## 🚀 Основные возможности

- **Фреймворк**: Aiogram 3.18.0
- **Базы данных**:
  - PostgreSQL (asyncpg 0.30.0)
  - SQLite (aiosqlite 0.21.0)
- **ORM**: SQLAlchemy 2.0.39
- **Миграции**: Alembic 1.15.1
- **Локализация**: Babel 2.17.0 (i18n)
- **Конфигурация**: Pydantic 2.10.6
- **Логирование**: Встроенная система с ротацией логов
- **Docker**: Готовый конфиг для развертывания

## 📋 Требования

- Python 3.8+
- Docker (опционально)
- Git

## 🛠 Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/zhandos256/templateaiogram
cd templateaiogram
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

3. Создайте файл `.env` и настройте переменные окружения:

```env
BOT_TOKEN=your_bot_token
DB_TYPE=sqlite  # или postgres
POSTGRES_DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres  # если используете PostgreSQL
DEBUG=True  # режим отладки
TIMEZONE=Asia/Almaty  # часовой пояс
```

4. Запустите миграции:

```bash
alembic upgrade head
```

5. Запустите бота:

```bash
python src/main.py
```

### Запуск через Docker

1. Создайте файл `.env` на основе примера выше и настройте переменные окружения:

```env
# Bot settings
BOT_TOKEN=your_bot_token
DEBUG=True
TIMEZONE=Asia/Almaty
POLLING_TIMEOUT=5

# Database settings
DB_TYPE=sqlite  # или postgres
POSTGRES_DB_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/postgres

# PostgreSQL settings (если используется PostgreSQL)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

2. Соберите и запустите контейнеры:

```bash
docker-compose build
docker-compose up
```

> **Примечание**: Все настройки теперь берутся из файла `.env`. Это позволяет легко менять конфигурацию без изменения `docker-compose.yml`.

## 🌍 Локализация

### Добавление нового языка

1. Извлеките строки для перевода:

```bash
pybabel extract --input-dirs=. -o locales/messages.pot
```

2. Создайте новый файл перевода:

```bash
pybabel init -i locales/messages.pot -d locales -D messages -l kk
```

3. Отредактируйте файл `locales/kk/LC_MESSAGES/messages.po`

4. Скомпилируйте переводы:

```bash
pybabel compile -d locales -D messages
```

## 📁 Структура проекта

```text
src/
├── config/           # Конфигурация приложения
├── database/         # Работа с базой данных
├── filters/          # Пользовательские фильтры
├── handlers/         # Обработчики команд
├── keyboards/        # Клавиатуры
├── locales/         # Файлы локализации
├── middleware/      # Middleware
├── services/        # Бизнес-логика
└── utils/           # Вспомогательные функции
```

## 🔧 Настройка

### База данных

- По умолчанию используется SQLite
- Для PostgreSQL измените `DB_TYPE=postgres` в `.env`
- URL базы данных PostgreSQL: `postgresql+asyncpg://postgres:postgres@localhost:5432/postgres`

### Логирование

- Логи сохраняются в директории `logs/`
- Формат: `YYYY-MM-DD.log`
- Режим отладки: `DEBUG=True` в `.env`

### Локализация

- По умолчанию: русский язык
- Файлы переводов: `locales/`
- Домен сообщений: `messages`

### Дополнительные настройки

- Часовой пояс: `TIMEZONE=Asia/Almaty`
- Таймаут поллинга: `POLLING_TIMEOUT=5`
- Режим отладки: `DEBUG=True`

## 🔧 Настройка окружения

### Разработка

1. Скопируйте `.env.example` в `.env`:

```bash
cp .env.example .env
```

2. Настройте переменные окружения в `.env`:

```env
BOT_TOKEN=your_bot_token
DEBUG=True
TIMEZONE=Asia/Almaty
POLLING_TIMEOUT=5
DB_TYPE=sqlite  # или postgres
```

### Продакшен

1. Создайте файл `.env.prod` с продакшен-настройками:

```env
BOT_TOKEN=your_bot_token
DEBUG=False
TIMEZONE=Asia/Almaty
POLLING_TIMEOUT=30
DB_TYPE=postgres
POSTGRES_DB_URL=postgresql+asyncpg://postgres:${POSTGRES_PASSWORD}@postgres:5432/postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_strong_password_here
POSTGRES_DB=postgres
```

2. Запустите с продакшен-конфигурацией:

```bash
docker-compose --env-file .env.prod up -d
```

> **Важно**:
>
> - `.env` и `.env.prod` файлы не должны попадать в репозиторий
> - Добавьте их в `.gitignore`
> - Храните `.env.prod` в безопасном месте
> - Используйте разные токены и пароли для разработки и продакшена

## 📝 Лицензия

MIT License
