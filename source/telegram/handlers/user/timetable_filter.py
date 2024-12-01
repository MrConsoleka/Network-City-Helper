import logging, os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from source.telegram.keyboards.reply import menu
from source.telegram.filters import AuthFilterMessage


timetable_user_filter = Router()


logger = logging.getLogger(__name__)


@timetable_user_filter.message(F.text == "Уроки", AuthFilterMessage(auth=True))
async def timateble_filter(message: Message) -> None:

    await message.delete()

    image_path = "source/data/images/расписание_уроков.png"

    if not os.path.exists(image_path):
        await message.answer("Нету изображения :(")
    else:
        image_from_pc = FSInputFile(image_path)
        await message.answer_photo(image_from_pc, caption="Расписание уроков")