from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


timetable_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="yes")],
    [InlineKeyboardButton(text="Нет", callback_data="no")],
])
