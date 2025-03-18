from datetime import datetime

import pytz
from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from config.const import settings


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, doc="Уникальный идентификатор пользователя в базе данных")
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(pytz.timezone(settings.TIMEZONE)), doc="Дата и время создания записи")
    tg_userid: Mapped[int] = mapped_column(BigInteger, unique=True, index=True, doc="Идентификатор пользователя в Telegram")
    username: Mapped[str] = mapped_column(String(length=64), default="-", nullable=True, doc="Имя пользователя в Telegram")
    first_name: Mapped[str] = mapped_column(String(length=255), default="-", nullable=True, doc="Имя пользователя")
    last_name: Mapped[str] = mapped_column(String(length=255), default="-", nullable=True, doc="Фамилия пользователя")
    language: Mapped[str] = mapped_column(String(length=2), default="ru", nullable=True, doc="Язык пользователя")
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, doc="Является ли пользователь администратором")
    last_action: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(pytz.timezone(settings.TIMEZONE)), doc="Дата и время последнего действия пользователя")