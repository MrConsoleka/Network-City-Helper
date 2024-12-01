from aiogram.filters import Filter
from aiogram import types
from aiogram.fsm.context import FSMContext

from source.misc import get_keys
from source.db import get_user, set_user
from source.telegram.keyboards.inline import policy, auth


class AuthFilterMessageFSM(Filter):
    def __init__(self, auth: bool) -> None:
        self.auth = auth

    async def __call__(self, message: types.Message, state: FSMContext) -> bool:

        user_id = message.from_user.id

        await set_user(user_id)

        user = await get_user(user_id)

        if user.role == "unauth":
            return True == self.auth

        else:
            await state.clear()
            await message.delete()
            await message.answer(
                f"Вы уже зарегестрированны!"
            )
