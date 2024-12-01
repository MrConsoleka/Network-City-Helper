from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from source.services.netschoolapi import check_netschoolapi
from source.telegram.keyboards.inline import auth, auth_stop
from source.services.cryptography import encryption
import source.telegram.keyboards.inline as kb
from source.db import get_user, update_auth
from source.telegram.filters import AuthFilterMessageFSM, AuthFilterCallbackFSM
from source.telegram.states import Auth


auth_callback = Router()


@auth_callback.callback_query(F.data == "auth_stop", AuthFilterCallbackFSM(auth=True))
async def auth_stop(callback: CallbackQuery, state: FSMContext):

    await callback.answer("")

    await state.clear()

    await callback.message.edit_text(
        text="Вы отменили авторизацию!\nЧто бы начать пользоваться ботом, <b>авторизуйтесь пожалуйста!</b>",
        reply_markup=kb.auth)


@auth_callback.callback_query(F.data == "auth_start", AuthFilterCallbackFSM(auth=True))
async def auth_start(callback: CallbackQuery, state: FSMContext):

    await callback.answer("")

    await state.set_state(Auth.login)
    msg = await callback.message.edit_text(
        text="Отправь мне свой логин от платформы Сетевой Город!",
        reply_markup=kb.auth_stop
    )
    await state.update_data(message_id=msg.message_id)


@auth_callback.message(Auth.login, AuthFilterMessageFSM(auth=True))
async def auth_input(message: Message, state: FSMContext, bot: Bot):

    await state.update_data(login=message.text)

    data = await state.get_data()

    await message.delete()

    await state.set_state(Auth.password)

    msg = await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=data["message_id"],
        text="Отправь мне свой пароль от платформы Сетевой Город!",
        reply_markup=kb.auth_stop
    )

    await state.update_data(message_id=msg.message_id)


@auth_callback.message(Auth.password, AuthFilterMessageFSM(auth=True))
async def auth_end(message: Message, state: FSMContext, bot: Bot):

    await state.update_data(password=message.text)

    data = await state.get_data()

    await message.delete()

    auth_netschool_check = await check_netschoolapi(data['login'], data['password'])

    if auth_netschool_check == "AuthError":
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=data["message_id"],
            text=f"<b>Ошибка авторизации! Неверный логин или пароль</b>"
        )
        await state.clear()

    elif auth_netschool_check == "Error":
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=data["message_id"],
            text=f"<b>Ошибка авторизации!</b>"
        )
        await state.clear()

    else:

        encrypted_password = await encryption(data['password'])

        if not encrypted_password:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=data["message_id"],
                text=f"Произошла ошибка во время шифрования пароля!"
            )
            await state.clear()

        else:

            role, name, surname, clas = auth_netschool_check

            await update_auth(message.from_user.id, data['login'], encrypted_password, role, name, surname, clas)

            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=data["message_id"],
                text=f"<b>Вы успешно зарегестрировались!</b>\n<i>Используй команду /menu</i>"
            )

            await state.clear()
