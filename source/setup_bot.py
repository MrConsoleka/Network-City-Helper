import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from apscheduler.triggers.cron import CronTrigger
from functools import partial

from source.misc import *
from source.telegram.handlers.user import *
from source.telegram.handlers.admin import *
from source.telegram.keyboards.callback import *
from source.telegram.middlewares import ThrottlingMiddlewareMessage, ThrottlingMiddlewareButton
from source.db import create_db, get_notice_users
from source.services.schedule import scheduler, send_overdue_message


logger = logging.getLogger(__name__)


bot = Bot(token=get_keys().BOT_TOKEN, default=DefaultBotProperties(parse_mode=parse_mode()))


dp = Dispatcher()


dp.include_routers(start_user_command, policy_callback, auth_callback,
                   menu_user_command, homework_user_filter, timetable_load_admin_command,
                   timetable_user_filter, holidays_user_filter, bells_user_filter,
                   bells_load_admin_command, holidays_load_admin_command, mark_user_filter,
                   overdue_user_filter, settings_callback, profile_user_filter,
                   announcement_admin_command, timetable_callback, help_user_command)


async def on_startup(bot):
    logger.info("Bot start")

    await create_db()

    scheduler.add_job(partial(send_overdue_message, bot), CronTrigger(day_of_week='mon,wed,fri', hour=16, minute=0))

    scheduler.start()


async def on_shutdown(bot):
    logger.info("Bot stop")


async def setup() -> None:

    await logger_setup()

    dp.startup.register(on_startup)

    dp.shutdown.register(on_shutdown)

    dp.message.middleware(ThrottlingMiddlewareMessage())

    dp.callback_query.middleware(ThrottlingMiddlewareButton())

    await bot.delete_webhook(drop_pending_updates=True)

    await setup_commands(bot=bot)

    await dp.start_polling(bot)
