from aiogram.types import BotCommand
from dataclasses import dataclass, field
from typing import List, Optional
from source.misc import get_keys
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from aiogram import Bot
from sqlalchemy.ext.asyncio import create_async_engine


@dataclass
class CommandsMenu:
    """Manages bot commands for different user types."""
    user_commands: List[BotCommand] = field(default_factory=lambda: [
        BotCommand(command="start", description="Начать"),
        BotCommand(command="menu", description="Меню"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="logout", description="Выйти"),
    ])
    admin_commands: List[BotCommand] = field(default_factory=lambda: [
        BotCommand(command="start", description="Начать"),
        BotCommand(command="menu", description="Меню"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="logout", description="Выйти"),
        BotCommand(command="bells_load", description="Загрузить расписание звонков"),
        BotCommand(command="holidays_load", description="Загрузить расписание каникул"),
        BotCommand(command="timetable_load", description="Загрузить расписание уроков"),
    ])

    async def set_commands(self, bot: Bot, admin_ids: Optional[List[int]] = None) -> None:
        """Sets bot commands for default and admin scopes."""
        await bot.set_my_commands(self.user_commands, scope=BotCommandScopeDefault())
        if admin_ids:
            for admin_id in admin_ids:
                try:
                    await bot.set_my_commands(self.admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
                except Exception as e:
                    print(f"Error setting commands for admin {admin_id}: {e}")


@dataclass
class DatabaseURL:
    """Represents database connection URL."""
    sql: str
    lib: str
    login: str
    password: str
    host: str
    port: int
    name: str

    def get_url(self) -> str:
        """Returns the database connection URL."""
        return f"{self.sql}+{self.lib}://{self.login}:{self.password}@{self.host}:{self.port}/{self.name}"


@dataclass
class ParseMode:
    """Manages parse mode for bot messages."""
    mode: str = "HTML"

    def get_mode(self) -> str:
        """Returns the parse mode."""
        return self.mode.upper() if self.mode.upper() in ("HTML", "MARKDOWNV2") else "HTML"


async def setup_commands(bot: Bot) -> None:
    """Sets up bot commands."""
    keys = get_keys()
    await CommandsMenu().set_commands(bot, keys.ADMINS_ID)


def db_url() -> None:
    """Sets up database connection URL."""
    keys = get_keys()
    url = DatabaseURL(keys.DB_SQL, keys.DB_LIB, keys.DB_LOGIN, keys.DB_PASSWORD, keys.DB_HOST, keys.DB_PORT,
                      keys.DB_NAME).get_url()
    return url


def parse_mode() -> None:
    """Sets up parse mode."""
    keys = get_keys()
    mode = ParseMode(keys.PARSE_MODE).get_mode()
    return mode
