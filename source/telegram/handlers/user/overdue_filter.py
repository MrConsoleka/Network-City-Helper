import logging
from aiogram import Router, F
from aiogram.types import Message
from source.db import get_user
from source.telegram.filters import AuthFilterMessage
from source.services.cryptography import decryption
from source.services.netschoolapi import overdue_netschoolapi


overdue_user_filter = Router()


logger = logging.getLogger(__name__)


@overdue_user_filter.message(F.text == "Просрочка", AuthFilterMessage(auth=True))
async def overdue_filter(message: Message) -> None:

    await message.delete()

    msg = await message.answer(text="<b>Секундочку, бот ищет данные...</b>")

    user = await get_user(message.from_user.id)

    password = await decryption(user.password)

    overdue = await overdue_netschoolapi(user.login, password)

    if overdue == "AuthError":
        await message.answer(
            text=f"<b>Ошибка авторизации! Неверный логин или пароль</b>"
        )

    elif overdue == "Error":
        await message.answer(
            text=f"<b>Ошибка авторизации!</b>"
        )

    else:
        try:
            await msg.delete()
        except Exception as e:
            pass
        await message.answer(text=overdue)


