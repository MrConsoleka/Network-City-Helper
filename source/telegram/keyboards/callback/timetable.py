import asyncio, os
from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile

from source.telegram.filters import AdminFilterCallback
from source.db import get_notice_users


timetable_callback = Router()


@timetable_callback.callback_query(F.data == "yes", AdminFilterCallback(admin=True))
async def yes(callback: CallbackQuery, bot: Bot):
    await callback.answer("")

    image_path = "source/data/images/расписание_уроков.png"

    if not os.path.exists(image_path):
        await callback.message.edit_text("Нету изображения для рассылки :(")
        return

    await callback.message.edit_text(text=f"<b>Рассылка расписания уроков запущена!</b>")

    try:

        user_ids = await get_notice_users(column_id="notice_timetable")

        if not user_ids:
            return

        for user_id in user_ids:
            image_from_pc = FSInputFile(image_path)
            await bot.send_photo(user_id, photo=image_from_pc, caption="Новое расписание уроков!")

    except AttributeError as e:
        logger.warning(f"Нет пользователей, которым нужно отправить уведомление! {e}")

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


@timetable_callback.callback_query(F.data == "no", AdminFilterCallback(admin=True))
async def no(callback: CallbackQuery):
    await callback.answer("")

    await callback.message.edit_text(text=f"<b>Рассылка расписания уроков отменена!</b>")