import logging
from aiogram import html, Router
from aiogram.filters import Command
from aiogram.types import Message


help_user_command = Router()


logger = logging.getLogger(__name__)


@help_user_command.message(Command("help"))
async def help_cmd(message: Message) -> None:

    await message.delete()

    await message.answer(
        text=f"👋 Привет, <b>{message.from_user.full_name}</b>! \n\n🤖 <b>Сетевой Город Helper</b> - некоммерческий проект, разработанный для помощи в учебе. \n\n<b>💻 Вот мои команды:</b>\n• /start - начать\n• /help - помощь\n• /logout - выйти из аккаунта \n<blockquote><i>При выходе из аккаунта ваши данные удаляются из базы.</i></blockquote>\n• /menu - получить клавиатуру для взаимодействия с ботом.\n\n👤 Мой разработчик: <a href='https://t.me/MrEnderman_YT'>@MrEnderman_YT</a>\n\n💾 Мой исходный код: <a href='https://github.com/MrEnderman-YT/Network-City-Helper'>github</a>\n\n<i>⚠️ Если наблюдаются проблемы в работе бота, напиши разработчику!</i>",
        disable_web_page_preview=True)

