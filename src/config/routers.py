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

main_router.include_router(admin_router)
main_router.include_router(start_router)
main_router.include_router(help_router)
main_router.include_router(about_router)
main_router.include_router(lang_router)
main_router.include_router(cancel_router)
main_router.include_router(echo_router)
main_router.include_router(menu_router)
main_router.include_router(settings_router)