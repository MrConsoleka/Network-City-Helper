import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from source.db import get_user, update_url
from source.telegram.filters import AuthFilterMessage
from source.services.cryptography import decryption
from source.services.aiograph import edit_aiograph, diary_aiograph
from source.services.netschoolapi import diary_day_netschoolapi, diary_monthy_netschoolapi, diary_tweek_netschoolapi


homework_user_filter = Router()


logger = logging.getLogger(__name__)


@homework_user_filter.message(F.text == "Д/З завтра", AuthFilterMessage(auth=True))
async def homework_filter(message: Message) -> None:

    await message.delete()

    msg = await message.answer(text="<b>Секундочку, бот ищет данные...</b>")

    user = await get_user(message.from_user.id)

    password = await decryption(user.password)

    homework = await diary_day_netschoolapi(user.login, password)

    if homework == "AuthError":
        await message.answer(text=f"<b>Ошибка авторизации! Неверный логин или пароль</b>")

    elif homework == "Error":
        await message.answer(text=f"<b>Ошибка авторизации!</b>")

    elif homework == "Error fetching":
        await message.answer(text=f"<b>Ошибка получения данных!</b>")

    else:
        try:
            await msg.delete()
        except Exception as e:
            pass

        user = await get_user(message.from_user.id)

        if not user.url_aiograph:

            url, token = await diary_aiograph(homework, message.from_user.id)

            await update_url(message.from_user.id, url, token)

            homework_b = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + url)]])

            await message.answer(text=f"<b>Ваше дз на завтра!</b>", reply_markup=homework_b)

        elif user.url_aiograph:

            await edit_aiograph(message.from_user.id, homework, user.url_aiograph, user.token_aiograph)

            homework_b = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + user.url_aiograph)]])

            await message.answer(text=f"<b>Ваше дз на завтра!</b>", reply_markup=homework_b)


@homework_user_filter.message(F.text == "Д/З неделя", AuthFilterMessage(auth=True))
async def filter_homework_handler2(message: Message) -> None:

    await message.delete()

    msg = await message.answer(text="<b>Секундочку, бот ищет данные...</b>")

    user = await get_user(message.from_user.id)

    password = await decryption(user.password)

    homework = await diary_tweek_netschoolapi(user.login, password)

    if homework == "AuthError":
        await message.answer(text=f"<b>Ошибка авторизации! Неверный логин или пароль</b>")

    elif homework == "Error":
        await message.answer(text=f"<b>Ошибка авторизации!</b>")

    elif homework == "Error fetching":
        await message.answer(text=f"<b>Ошибка получения данных!</b>")

    else:
        try:
            await msg.delete()
        except Exception as e:
            pass

        user = await get_user(message.from_user.id)

        if not user.url_aiograph:

            url, token = await diary_aiograph(homework, message.from_user.id)

            await update_url(message.from_user.id, url, token)

            homework_b = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + url)]])

            await message.answer(text=f"<b>Ваше дз на неделю!</b>", reply_markup=homework_b)

        elif user.url_aiograph:

            await edit_aiograph(message.from_user.id, homework, user.url_aiograph, user.token_aiograph)

            homework_b = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + user.url_aiograph)]])

            await message.answer(text=f"<b>Ваше дз на неделю!</b>", reply_markup=homework_b)


@homework_user_filter.message(F.text == "Д/З месяц", AuthFilterMessage(auth=True))
async def filter_homework_handler3(message: Message) -> None:

    await message.delete()

    msg = await message.answer(text="<b>Секундочку, бот ищет данные...</b>")

    user = await get_user(message.from_user.id)

    password = await decryption(user.password)

    homework = await diary_monthy_netschoolapi(user.login, password)

    if homework == "AuthError":
        await message.answer(text=f"<b>Ошибка авторизации! Неверный логин или пароль</b>")

    elif homework == "Error":
        await message.answer(text=f"<b>Ошибка авторизации!</b>")

    elif homework == "Error fetching":
        await message.answer(text=f"<b>Ошибка получения данных!</b>")

    else:
        try:
            await msg.delete()
        except Exception as e:
            pass

        user = await get_user(message.from_user.id)

        if not user.url_aiograph:

            url, token = await diary_aiograph(homework, message.from_user.id)

            await update_url(message.from_user.id, url, token)

            homework_b = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + url)]])

            await message.answer(text=f"<b>Ваше дз на месяц!</b>", reply_markup=homework_b)

        elif user.url_aiograph:

            await edit_aiograph(message.from_user.id, homework, user.url_aiograph, user.token_aiograph)

            homework_b = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📖 Читать", url="https://telegra.ph/" + user.url_aiograph)]])

            await message.answer(text=f"<b>Ваше дз на месяц!</b>", reply_markup=homework_b)

