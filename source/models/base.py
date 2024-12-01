from sqlalchemy import DateTime, Float, String, Text, func, BigInteger, VARCHAR, BOOLEAN
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role: Mapped[str] = mapped_column(VARCHAR(10), default="unauth")
    login: Mapped[str] = mapped_column(Text, nullable=True)
    password: Mapped[str] = mapped_column(Text, nullable=True)
    name: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    surname: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    clas: Mapped[str] = mapped_column(VARCHAR(2), nullable=True)
    privacy_policy: Mapped[int] = mapped_column(BOOLEAN, default=0)
    notice_timetable: Mapped[int] = mapped_column(BOOLEAN, default=0)
    notice_announcement: Mapped[int] = mapped_column(BOOLEAN, default=0)
    notice_overdue_assigment: Mapped[int] = mapped_column(BOOLEAN, default=0)
    url_aiograph: Mapped[str] = mapped_column(Text, nullable=True)
    token_aiograph: Mapped[str] = mapped_column(Text, nullable=True)
