import logging
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from source.telegram.filters import AdminFilterMessage


bells_load_admin_command = Router()


logger = logging.getLogger(__name__)


@bells_load_admin_command.message(Command("bells_load"), AdminFilterMessage(admin=True))
async def command_holidays_handler(message: Message, bot: Bot) -> None:

    await message.delete()

    if message.photo:
        await bot.download(message.photo[-1], destination=f"source/data/images/расписание_звонков.png")

        await message.answer(text=f"<b>Расписание звонков загружено!</b>")
    else:
        await message.answer(text="Прикрепите фотографию к команде <code>/bells_load</code>")

