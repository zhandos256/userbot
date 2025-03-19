from typing import Any, Dict

from aiogram.types import TelegramObject, User as AiogramUser
from aiogram.utils.i18n import I18n, I18nMiddleware

from config.const import settings
from database.queries import get_user_lang


class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        user: AiogramUser = data["event_from_user"]
        return await get_user_lang(tg_userid=user.id) or settings.DEFAULT_LOCALE


i18n = I18n(path=settings.LOCALES_DIR, default_locale=settings.DEFAULT_LOCALE, domain=settings.DOMAIN_MESSAGES)
i18n_middleware = CustomI18nMiddleware(i18n=i18n)
