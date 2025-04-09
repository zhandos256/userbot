from typing import Any, Dict

from aiogram.utils.i18n import I18n, I18nMiddleware
from aiogram.types import TelegramObject, User as AiogramUser

from config.user_settings import settings, LOCALES_DIR
from database.user_queries import get_user_lang


class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        user: AiogramUser = data["event_from_user"]
        return await get_user_lang(tg_userid=user.id) or settings.default_locale


i18n = I18n(path=LOCALES_DIR, default_locale=settings.default_locale, domain=settings.default_locale)
i18n_middleware = CustomI18nMiddleware(i18n=i18n)
