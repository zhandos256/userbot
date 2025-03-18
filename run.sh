#!/bin/bash

# Создание необходимых директорий
mkdir -p ./src/migrations/versions ./src/locales src/logs

# Переход в директорию src
cd ./src

# Проверка наличия файлов .py в директории migrations/versions
if ls migrations/versions/*.py 1>/dev/null 2>&1; then
    echo "Миграции уже существуют, пропускаем создание новой."
else
    # Если миграций нет, создаем новую
    alembic revision --autogenerate -m "initial"
    alembic upgrade head
fi

python main.py
