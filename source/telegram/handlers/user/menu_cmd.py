import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from source.telegram.keyboards.reply import menu
from source.telegram.filters import AuthFilterMessage


menu_user_command = Router()


logger = logging.getLogger(__name__)


@menu_user_command.message(Command("menu"), AuthFilterMessage(auth=True))
async def menu_cmd(message: Message) -> None:

    await message.delete()

    await message.answer(text=f"<b>Меню было выданно!</b>", reply_markup=menu)

