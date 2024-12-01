import logging
from aiogram import Router, F
from aiogram.types import Message

from source.telegram.keyboards.reply import menu
from source.telegram.filters import AuthFilterMessage


mark_user_filter = Router()


logger = logging.getLogger(__name__)


@mark_user_filter.message(F.text == "Оценки", AuthFilterMessage(auth=True))
async def mark_filter(message: Message) -> None:

    await message.delete()

    await message.answer("Данная функция еще не реализованна, но мой разработчик MrEnderman трудится на ее созданием! :(")
