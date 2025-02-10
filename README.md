# Aiogram 3.1.1 template

## Dependencies

- **Aiogram** - 3.1.1 version
- **SQLAlchemy** - Orm mapped query
- **Asyncpg** - Postgres async driver
- **Aiosqlite** - Sqlite async driver
- **Alembic** - Database migrations
- **Babel** - I18n localization

## Requirements

Python 3.8 or higher

## Close repo

```bash
git clone https://github.com/zhandos256/templateaiogram
cd templateaiogram
```

Get your real token from @Botfaterh and insert your token into docker-compose.yml:

```bash
environment:
  - BOT_TOKEN=YOUR_BOT_TOKEN
```

## Build and up

```bash
docker-compose build && docker-compose up
```
