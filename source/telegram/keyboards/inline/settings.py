from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from source.db import get_user


settings_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")],
    [InlineKeyboardButton(text="🚪 Выйти", callback_data="logout")],
])


async def create_change_settings_menu(user_id):

    user = await get_user(user_id)

    notice_overdue_assigment = "вкл." if user.notice_overdue_assigment else "выкл."
    notice_announcement = "включено" if user.notice_announcement else "выключено"
    notice_timetable = "включено" if user.notice_timetable else "выключено"

    change_settings_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Уведомление 'Просроченные задания' {notice_overdue_assigment}", callback_data="settings_notification_overdue_assignments")],
        [InlineKeyboardButton(text=f"Уведомление 'События' {notice_announcement}", callback_data="settings_notification_announcement")],
        [InlineKeyboardButton(text=f"Уведомление 'Расписание' {notice_timetable}", callback_data="settings_notification_timetable")],
        [InlineKeyboardButton(text=f"🔙 Назад", callback_data="settings_back")],

    ])

    return change_settings_menu
