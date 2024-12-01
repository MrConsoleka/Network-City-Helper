from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from source.db import get_user, clear_user, update_notice

import source.telegram.keyboards.inline as kb

from source.telegram.filters import AuthFilterCallback

import asyncio


settings_callback = Router()


@settings_callback.callback_query(F.data == "logout")
async def logout(callback: CallbackQuery):
    await callback.answer("")

    await clear_user(callback.from_user.id)

    await callback.message.edit_text(text=f"<b>Вы вышли из аккаунта!</b>")

    msg = await callback.message.answer(text=f"Ваша клавиатура была удалени!", reply_markup=types.ReplyKeyboardRemove())

    await msg.delete()


@settings_callback.callback_query(F.data == "settings_back", AuthFilterCallback(auth=True))
async def settings_back(callback: CallbackQuery):
    await callback.answer("")

    user = await get_user(callback.from_user.id)

    if user.role is None:
        user.role = "неизвестно"

    elif user.name is None:
        user.name = "неизвестно"

    elif user.surname is None:
        user.surname = "неизвестно"

    elif user.clas is None:
        user.clas = "неизвестно"

    await callback.message.edit_text(
        text=f"<b>┏┫★ ПРОФИЛЬ:</b>\n\n<b>👤 • Никнейм:</b>   <code>{callback.from_user.full_name}</code>\n<b>🔑 • ID:</b>   <code>{callback.from_user.id}</code>\n<b>⚡️ • Статус:</b>   <code>{user.role}</code>\n<b>🎫 • Имя:</b>   <code>{user.name}</code>\n<b>🎫 • Фамилия:</b>   <code>{user.surname}</code>\n<b>🏫 • Школа:</b>   <code>МБОУ СОШ № 99 г. Челябинска</code>\n<b>🧰 • Класс:</b>   <code>{user.clas}</code>"
        , reply_markup=kb.settings_menu)


@settings_callback.callback_query(F.data == "settings", AuthFilterCallback(auth=True))
async def settings(callback: CallbackQuery):
    await callback.answer("")

    change_settings_menu = await kb.create_change_settings_menu(callback.from_user.id)

    await callback.message.edit_text(
        text="<b>┏┫★ НАСТРОЙКИ:</b>\n\n<b>🔔 • Настройте уведомления:</b>\n┗┫Уведомления о просроченных заданиях.\n┗┫Будьте в курсе событий.\n┗┫Узнавайте о новом расписании.\n\n<b>🔐 • Измените свои данные:</b>\n┗┫Можете сменить пароль.\n┗┫Можете обновить логин."
        , reply_markup=change_settings_menu
    )


@settings_callback.callback_query(F.data == "settings_notification_overdue_assignments", AuthFilterCallback(auth=True))
async def settings_menu(callback: CallbackQuery):
    await callback.answer("")

    await update_notice(callback.from_user.id, "notice_overdue_assigment")

    user = await get_user(callback.from_user.id)

    notice_overdue_assigment = "включили" if user.notice_overdue_assigment else "выключили"

    change_settings_menu = await kb.create_change_settings_menu(callback.from_user.id)

    await callback.message.edit_text(
        text=f"<b>┏┫★ НАСТРОЙКИ:</b>\n\n<b>🔔 • Настройте уведомления:</b>\n┗┫Уведомления о просроченных заданиях.\n┗┫Будьте в курсе событий.\n┗┫Узнавайте о новом расписании.\n\n<b>🔐 • Измените свои данные:</b>\n┗┫Можете сменить пароль.\n┗┫Можете обновить логин.\n\n💾 • <i>Вы успешно {notice_overdue_assigment} уведомления 'Просроченные задания'</i>"
        , reply_markup=change_settings_menu
    )


@settings_callback.callback_query(F.data == "settings_notification_announcement", AuthFilterCallback(auth=True))
async def settings_menu(callback: CallbackQuery):
    await callback.answer("")

    await update_notice(callback.from_user.id, "notice_announcement")

    user = await get_user(callback.from_user.id)

    notice_announcement = "включили" if user.notice_announcement else "выключили"

    change_settings_menu = await kb.create_change_settings_menu(callback.from_user.id)

    await callback.message.edit_text(
        text=f"<b>┏┫★ НАСТРОЙКИ:</b>\n\n<b>🔔 • Настройте уведомления:</b>\n┗┫Уведомления о просроченных заданиях.\n┗┫Будьте в курсе событий.\n┗┫Узнавайте о новом расписании.\n\n<b>🔐 • Измените свои данные:</b>\n┗┫Можете сменить пароль.\n┗┫Можете обновить логин.\n\n💾 • <i>Вы успешно {notice_announcement} уведомления 'События'</i>"
        , reply_markup=change_settings_menu
    )


@settings_callback.callback_query(F.data == "settings_notification_timetable", AuthFilterCallback(auth=True))
async def settings_menu(callback: CallbackQuery):
    await callback.answer("")

    await update_notice(callback.from_user.id, "notice_timetable")

    user = await get_user(callback.from_user.id)

    notice_timetable = "включили" if user.notice_timetable else "выключили"

    change_settings_menu = await kb.create_change_settings_menu(callback.from_user.id)

    await callback.message.edit_text(
        text=f"<b>┏┫★ НАСТРОЙКИ:</b>\n\n<b>🔔 • Настройте уведомления:</b>\n┗┫Уведомления о просроченных заданиях.\n┗┫Будьте в курсе событий.\n┗┫Узнавайте о новом расписании.\n\n<b>🔐 • Измените свои данные:</b>\n┗┫Можете сменить пароль.\n┗┫Можете обновить логин.\n\n💾 • <i>Вы успешно {notice_timetable} уведомления 'Новое расписание'</i>"
        , reply_markup=change_settings_menu
    )
