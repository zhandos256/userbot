# Шаблон для телеграм бота на базе библиотеки Aiogram 3.1.1

- **SQLAlchemy**: ORM для работы с базой данных.
- **AioSQLite**: Асинхронный клиент для работы с SQLite.
- **Alembic**: Инструмент для управления миграциями базы данных.
- **Aiogram**: Фреймворк для разработки Telegram-ботов.
- **Aioredis**: Key-value база данных для кэша.
- **Babel**: Для локализации текста.

## Требования

Убедитесь, что у вас установлена версия Python 3.8 или выше.

## Настройка

1. **Клонируйте репозиторий**:

    ```bash
    git clone https://github.com/zhandos256/templateaiogram.git
    cd templateaiogram
    ```

2. **Добавляем доступ на выполнению скриптам**:

    ```bash
    sudo chmod +x run.sh
    ```

3. **Установка зависисмостей и инициализация базы данных**:

    Запустите init.sh

    ```bash
    ./init.sh
    ```
    > init.sh запускается всего 1

    > Что делает init.sh:
    > - Создает новый python environment
    > - Устанавливает зависисмости из requirements.txt
    > - Накатывает начальную миграцию (alembic revision --autogenerate -m "initial")

4. **Настройка переменной окружения BOT_TOKEN**:

    Установите переменную окружения BOT_TOKEN в вашей системе.
    - На Windows:
        ```
        set BOT_TOKEN="YOUR_BOT_TOKEN"
        ```
    - На macOS и Linux:
        ```
        export BOT_TOKEN="YOUR_BOT_TOKEN"
        ```
    Замените YOUR_BOT_TOKEN на ваш реальный токен, который вы получили от @BotFather.

5. **Для запуска бота**:

    Для запуска бота выполните run.sh

    ```bash
    source run.sh
    ```

## Лицензия

Этот проект лицензируется на условиях лицензии MIT. Подробнее см. файл LICENSE.
