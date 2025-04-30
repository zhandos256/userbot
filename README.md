# Aiogram templtae 3.18.0

Modern template for development Telegram bots on based Aiogram 3.18.0. Includes all needed components for create scalable and supported bots.

## Main features

- **Framework**: Aiogram 3.18.0
- **Database**:
  - PostgreSQL (asyncpg 0.30.0)
  - SQLite (aiosqlite 0.21.0)
- **ORM**: SQLAlchemy 2.0.39
- **Migrations**: Alembic 1.15.1
- **Localization**: Babel 2.17.0 (i18n)
- **Configuration**: Pydantic 2.10.6
- **Logging**: Main features Built-in log rotation system
- **Docker**: Ready-made configuration for deployment

## 📋 Requirements

- Python 3.8+
- Docker (опционально)
- Git

## 🛠 Install and run

### Local run

1. Clone repository:

```bash
git clone https://github.com/zhandos256/templateaiogram
cd templateaiogram
```

2. Create virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

3. Create file `.env` and configure the environment variables:

```env
BOT_TOKEN=your_bot_token
DB_TYPE=sqlite  # или postgres
POSTGRES_DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres  # если используете PostgreSQL
DEBUG=True  # режим отладки
```

4. Start migrations:

```bash
alembic upgrade head
```

5. Start bot:

```bash
python src/main.py
```

### Start via docker

1. Create file `.env` based on the example above, set up the environment variables:

```env
# Bot settings
BOT_TOKEN=your_bot_token
DEBUG=True

# Database settings
DB_TYPE=sqlite  # или postgres
POSTGRES_DB_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/postgres

# PostgreSQL settings (если используется PostgreSQL)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

2. Build and start container:

```bash
docker-compose build
docker-compose up
```

> **Note**: All settings are now taken from the file `.env`. This makes it easy to change the configuration without changing the `docker-compose.yml'.

## 🌍 Localization

### Add new language

1. Extract the translation strings:

```bash
pybabel extract --input-dirs=. -o locales/messages.pot
```

2. Create a new translation file:

```bash
pybabel init -i locales/messages.pot -d locales -D messages -l kk
```

3. Edit the file `locales/kk/LC_MESSAGES/messages.po`

4. Compile the translations:

```bash
pybabel compile -d locales -D messages
```

## 📁 Project structure

```text
src/
├── config/           # App configuration
├── database/         # Work with database
├── filters/          # Custom Filters
├── handlers/         # Handlers
├── keyboards/        # Keyboards
├── locales/         # Localization files
├── middleware/      # Middlewares
├── services/        # Business logic
└── utils/           # Auxiliary functions
```

## 🔧 Settings

### Database

- By default used Sqlite database
- For use PostgreSQL change `DB_TYPE=postgres` in `.env` file
- Database URL PostgreSQL: `postgresql+asyncpg://postgres:postgres@localhost:5432/postgres`

### Logging

- Logs are saved in the directory `logs/`
- Log format: `YYYY-MM-DD.log`
- Debugging mode: `DEBUG=True` в `.env`

### Localization

- By default: russioan language
- Translation files: `locales/`
- Message domain: `messages`

## 🔧 Setting up the environment

### Development

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Set up environment variables in `.env`:

```env
BOT_TOKEN=your_bot_token
DEBUG=True
TIMEZONE=Asia/Almaty
POLLING_TIMEOUT=5
DB_TYPE=sqlite  # или postgres
```

### Production

1. Create file `.env.prod` with production settings:

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

2. Start with production configuration:

```bash
docker-compose --env-file .env.prod up -d
```

> **Important**:
>
> - `.env` and `.env.prod` files don't should be in repository
> - Add them to `.gitignore`
> - Keep `.env.prod` in a safe place
> - Use different tokens and passwords for development and production

## 📝 License

MIT License
