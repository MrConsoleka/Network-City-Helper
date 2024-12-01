import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, types
from source.services.netschoolapi import overdue_netschoolapi
from source.services.cryptography import decryption
from source.db import get_user, get_notice_users

logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()


async def send_overdue_message(bot: Bot):
    try:
        user_ids = await get_notice_users(column_id="notice_overdue_assigment")

        if not user_ids:
            logger.info("Нет пользователей для уведомления.")
            return

        for user_id in user_ids:
            try:
                user = await get_user(user_id)

                if user is None:
                    logger.warning(f"Пользователь с ID {user_id} не найден.")
                    continue

                password = await decryption(user.password)

                overdue = await overdue_netschoolapi(user.login, password)

                if overdue != "Нету просроченных заданий!":
                    await bot.send_message(user_id, text=overdue)
                else:
                    logger.info(f"Пользователь {user_id} не имеет просроченных заданий.")

            except Exception as e:
                logger.error(f"Ошибка при обработке пользователя с ID {user_id}: {e}")

    except Exception as e:
        logger.error(f"Произошла ошибка в функции отправки уведомлений: {e}")