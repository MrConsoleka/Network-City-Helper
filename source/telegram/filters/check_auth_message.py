from aiogram.filters import Filter
from aiogram import types
from aiogram.fsm.context import FSMContext

from source.misc import get_keys
from source.db import get_user, set_user
from source.telegram.keyboards.inline import policy, auth


class AuthFilterMessage(Filter):
    def __init__(self, auth: bool) -> None:
        self.auth = auth

    async def __call__(self, message: types.Message, state: FSMContext) -> bool:

        user_id = message.from_user.id

        await set_user(user_id)

        user = await get_user(user_id)

        if user.role in ["admin", "parent", "teacher", "student"]:

            return True == self.auth

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


