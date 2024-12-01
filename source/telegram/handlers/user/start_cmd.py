import logging
from aiogram import html, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from source.db.engine import set_user
from source.db import get_user
from source.telegram.keyboards.inline import policy, auth


start_user_command = Router()


logger = logging.getLogger(__name__)


@start_user_command.message(CommandStart())
async def start_cmd(message: Message) -> None:

    user_id = message.from_user.id

    await message.delete()

    await set_user(user_id)

    user = await get_user(user_id)

    if user.role in ["admin", "parent", "teacher", "student"]:

        await message.answer(
            f"Привет, <b>{message.from_user.full_name}</b>!\n<i>Вы уже зарегестрированны!</i>"
        )

    else:
        if user.privacy_policy == 0:

            await message.answer(
                f"👋 Привет, <b>{message.from_user.full_name}</b>! \n\n🤖 <b>Сетевой Город Helper</b> - некоммерческий проект, разработанный для помощи в учебе. \n\n<b>⚙️ Доступные возможности:</b>\n• Уведомления о просроченных заданиях\n• Уведомления о новом расписании\n• Просмотр домашнего задания\n• Просмотр расписания каникул и звонков\n• Калькулятор оценок\n• Отчет об оценках\n\n⛔️ Данный проект <b>не имеет</b> отношения к <b>«ИрТеху»</b>\n\n<b><i>⚠️ Что бы начать пользоваться ботом, вам нужно принять <u>политику конфедициальности</u></i></b>",
                reply_markup=policy
            )

        else:
            await message.answer(
                f"Что бы начать пользоваться ботом, <b>авторизуйтесь</b> пожалуйста!",
                reply_markup=auth
            )

