#!/bin/bash

# Функция для вывода ошибки и выхода
error_exit() {
    echo "Ошибка: $1" >&2
    exit 1
}

# Проверка наличия необходимых команд
command -v python >/dev/null 2>&1 || error_exit "Python не установлен"
command -v alembic >/dev/null 2>&1 || error_exit "Alembic не установлен"

# Создание необходимых директорий
echo "Создание необходимых директорий..."
mkdir -p ./src/migrations/versions ./src/locales ./src/logs || error_exit "Не удалось создать директории"

# Переход в директорию src
cd ./src || error_exit "Не удалось перейти в директорию src"

# Проверка наличия файла alembic.ini
if [ ! -f "alembic.ini" ]; then
    error_exit "Файл alembic.ini не найден"
fi

# Проверка наличия файлов .py в директории migrations/versions
if ls migrations/versions/*.py 1>/dev/null 2>&1; then
    echo "Миграции уже существуют, пропускаем создание новой."
else
    echo "Создание начальной миграции..."
    alembic revision --autogenerate -m "initial" || error_exit "Не удалось создать миграцию"
    echo "Применение миграции..."
    alembic upgrade head || error_exit "Не удалось применить миграцию"
fi

# Проверка наличия файла main.py
if [ ! -f "main.py" ]; then
    error_exit "Файл main.py не найден"
fi

# Проверка наличия переменных окружения
if [ -z "$BOT_TOKEN" ]; then
    error_exit "Переменная окружения BOT_TOKEN не установлена"
fi

echo "Запуск бота..."
python main.py || error_exit "Ошибка при запуске бота"
