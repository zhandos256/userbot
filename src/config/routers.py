from aiogram import Router

from handlers.admin.admin import router as admin_router
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.about import router as about_router
from handlers.users.lang import router as lang_router
from handlers.users.cancel import router as cancel_router
from handlers.users.echo import router as echo_router
from handlers.users.menu import router as menu_router
from handlers.users.settings import router as settings_router

main_router = Router()
"""Главный роутер, который объединяет все роутеры приложения."""

admin_routers = [
    admin_router,
]

# Группировка роутеров
user_routers = [
    start_router,
    help_router,
    menu_router,
    about_router,
    settings_router,
    lang_router,
    cancel_router,  # cancel_router должен быть всегда пред-послденим!
    echo_router,  # echo_router должен быть всегда последним!
]

# Регистрация роутеров
main_router.include_router(admin_router)
for router in user_routers:
    main_router.include_router(router)