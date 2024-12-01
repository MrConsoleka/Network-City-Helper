import logging
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from source.telegram.filters import AdminFilterMessage


holidays_load_admin_command = Router()


logger = logging.getLogger(__name__)


@holidays_load_admin_command.message(Command("holidays_load"), AdminFilterMessage(admin=True))
async def command_timetable_handler(message: Message, bot: Bot) -> None:

    await message.delete()

    if message.photo:
        await bot.download(message.photo[-1], destination=f"source/data/images/расписание_каникул.png")

        await message.answer(text=f"<b>Расписание каникул загружено!</b>")
    else:
        await message.answer(text="Прикрепите фотографию к команде <code>/holidays_load</code>")

