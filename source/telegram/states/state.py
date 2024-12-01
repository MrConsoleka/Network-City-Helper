from aiogram.fsm.state import State, StatesGroup


class Auth(StatesGroup):
    login = State()
    password = State()
