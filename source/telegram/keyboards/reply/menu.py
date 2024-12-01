from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Профиль")],
    [KeyboardButton(text="Уроки"), KeyboardButton(text="Звонки"), KeyboardButton(text="Каникулы")],
    [KeyboardButton(text="Д/З завтра"), KeyboardButton(text="Д/З неделя"), KeyboardButton(text="Д/З месяц")],
    [KeyboardButton(text="Просрочка"), KeyboardButton(text="Оценки")]
], resize_keyboard=True, input_field_placeholder="Выберите пункт меню")
