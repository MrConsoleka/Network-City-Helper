import logging
from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from source.telegram.filters import AdminFilterMessage
from source.db import get_notice_users

announcement_admin_command = Router()

logger = logging.getLogger(__name__)


@announcement_admin_command.message(Command("announcement"), AdminFilterMessage(admin=True))
async def command_announcement_handler(message: Message, command: CommandObject, bot: Bot) -> None:
    try:
        args = command.args

        if not args:
            await message.answer(
                text="Напишите текст объявления! \nПример: <code>/announcement Привет! Это объявление!</code>")
            return

        user_ids = await get_notice_users(column_id="notice_announcement")

        if not user_ids:
            await message.answer("Нет пользователей для уведомления.")
            return

        for user_id in user_ids:
            await bot.send_message(user_id, text="<b>Объявление:</b>\n" + " ".join(args))

    except AttributeError as e:
        logger.warning(f"Нет пользователей, которым нужно отправить уведомление! {e}")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
