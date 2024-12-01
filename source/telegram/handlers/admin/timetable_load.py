import logging
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from source.telegram.filters import AdminFilterMessage

from source.telegram.keyboards.inline import timetable_menu

timetable_load_admin_command = Router()


logger = logging.getLogger(__name__)


@timetable_load_admin_command.message(Command("timetable_load"), AdminFilterMessage(admin=True))
async def command_timetable_handler(message: Message, bot: Bot) -> None:

    await message.delete()

    if message.photo:
        await bot.download(message.photo[-1], destination=f"source/data/images/расписание_уроков.png")

        await message.answer(text=f"<b>Расписание уроков загружено!</b>")

        await message.answer(text=f"<b>Разослать расписание всем пользователям?</b>", reply_markup=timetable_menu)

    else:
        await message.answer(text="Прикрепите фотографию к команде <code>/timetable_load</code>")

