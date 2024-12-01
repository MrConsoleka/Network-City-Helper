from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

auth = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Авторизоваться (логин/пароль)", callback_data="auth_start")]])

auth_stop = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Отменить", callback_data="auth_stop")]])