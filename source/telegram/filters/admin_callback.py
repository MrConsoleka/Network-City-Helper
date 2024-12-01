from aiogram.filters import Filter
from aiogram import types
from source.misc import get_keys


class AdminFilterCallback(Filter):
    def __init__(self, admin: bool) -> None:
        self.admin = admin

    async def __call__(self, callback: types.CallbackQuery) -> bool:
        keys = get_keys()

        is_admin = callback.from_user.id in keys.ADMINS_ID

        if self.admin == is_admin:

            return True

        else:
            await callback.message.edit_text("Вы не админ!")

            return False
