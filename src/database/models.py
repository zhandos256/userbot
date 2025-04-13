from typing import Optional
from datetime import datetime

import pytz
from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String, Index
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from config.user_settings import TIMEZONE

# Константы для значений по умолчанию
DEFAULT_USERNAME = "-"
DEFAULT_FIRST_NAME = "-"
DEFAULT_LAST_NAME = "-"
DEFAULT_LANGUAGE = "ru"
DEFAULT_IS_ADMIN = False


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    # Индексы для оптимизации запросов
    __table_args__ = (
        Index('idx_users_tg_userid', 'tg_userid'),
        Index('idx_users_created', 'created'),
        Index('idx_users_last_action', 'last_action'),
    )

    id: Mapped[int] = mapped_column( Integer, primary_key=True, doc="Уникальный идентификатор пользователя в базе данных")
    created: Mapped[datetime] = mapped_column( DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone(TIMEZONE)), nullable=False, doc="Дата и время создания записи")
    tg_userid: Mapped[int] = mapped_column( BigInteger, unique=True, nullable=False, index=True, doc="Идентификатор пользователя в Telegram")
    username: Mapped[Optional[str]] = mapped_column( String(length=64), nullable=True, default=DEFAULT_USERNAME, doc="Имя пользователя в Telegram")
    first_name: Mapped[Optional[str]] = mapped_column( String(length=255), nullable=True, default=DEFAULT_FIRST_NAME, doc="Имя пользователя")
    last_name: Mapped[Optional[str]] = mapped_column( String(length=255), nullable=True, default=DEFAULT_LAST_NAME, doc="Фамилия пользователя")
    language: Mapped[str] = mapped_column( String(length=2), nullable=False, default=DEFAULT_LANGUAGE, doc="Язык пользователя")
    is_admin: Mapped[bool] = mapped_column( Boolean, nullable=False, default=DEFAULT_IS_ADMIN, doc="Является ли пользователь администратором")
    last_action: Mapped[datetime] = mapped_column( DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone(TIMEZONE)), nullable=False, doc="Дата и время последнего действия пользователя")