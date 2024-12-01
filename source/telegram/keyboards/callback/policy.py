from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from source.db import get_user, update_privacy

policy_callback = Router()


@policy_callback.callback_query(F.data == "policy")
async def policy(callback: CallbackQuery):
    user_id = callback.from_user.id

    user = await get_user(user_id)

    if not user.privacy_policy:
        await update_privacy(user_id)
        await callback.answer("Вы приняли политику конфиденциальности!", show_alert=True)
        await callback.message.edit_text(text="Что бы начать пользоваться ботом, <b>авторизуйтесь пожалуйста!</b>")

    elif user.privacy_policy:
        await callback.answer("Вы уже приняли политику конфиденциальности!", show_alert=True)
        await callback.message.edit_text(text="Что бы начать пользоваться ботом, <b>авторизуйтесь пожалуйста!</b>")