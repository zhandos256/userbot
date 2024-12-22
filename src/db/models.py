from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.today())
    tg_userid: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(length=32), default="-")
    first_name: Mapped[str] = mapped_column(String(length=255), default="-")
    last_name: Mapped[str] = mapped_column(String(length=255), default="-")
    language: Mapped[str] = mapped_column(String(length=2), default="ru")
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
