from aiogram.filters import Filter
from aiogram import types
from source.misc import get_keys


class AdminFilterMessage(Filter):
    def __init__(self, admin: bool) -> None:
        self.admin = admin

    async def __call__(self, message: types.Message) -> bool:
        keys = get_keys()

        is_admin = message.from_user.id in keys.ADMINS_ID

        if self.admin == is_admin:

            return True

        else:
            await message.answer("Вы не админ!")

            return False
