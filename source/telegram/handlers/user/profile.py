import logging
from aiogram import Router, F
from aiogram.types import Message

from source.telegram.keyboards.reply import menu
from source.telegram.filters import AuthFilterMessage
from source.db import get_user
from source.telegram.keyboards.inline import settings_menu


profile_user_filter = Router()


logger = logging.getLogger(__name__)


@profile_user_filter.message(F.text == "Профиль", AuthFilterMessage(auth=True))
async def profile_filter(message: Message):

    await message.delete()

    user = await get_user(message.from_user.id)

    if user.role is None:
        user.role = "неизвестно"

    elif user.name is None:
        user.name = "неизвестно"

    elif user.surname is None:
        user.surname = "неизвестно"

    elif user.clas is None:
        user.clas = "неизвестно"

    await message.answer(
        text=f"<b>┏┫★ ПРОФИЛЬ:</b>\n\n<b>👤 • Никнейм:</b>   <code>{message.from_user.full_name}</code>\n<b>🔑 • ID:</b>   <code>{message.from_user.id}</code>\n<b>⚡️ • Статус:</b>   <code>{user.role}</code>\n<b>🎫 • Имя:</b>   <code>{user.name}</code>\n<b>🎫 • Фамилия:</b>   <code>{user.surname}</code>\n<b>🏫 • Школа:</b>   <code>МБОУ СОШ № 99 г. Челябинска</code>\n<b>🧰 • Класс:</b>   <code>{user.clas}</code>"
        , reply_markup=settings_menu)
