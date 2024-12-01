import logging
import traceback
from aiogram import Router, F
from aiogram.types import Message, ErrorEvent
from aiogram.enums import ParseMode
from aiogram.exceptions import *
from aiogram.filters import ExceptionTypeFilter
from source.exceptions import MyCustomException


error_extra_event = Router()


logger = logging.getLogger(__name__)


@error_system_event.error(ExceptionTypeFilter(MyCustomException), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer("Oops, something went wrong!")


@error_system_event.error(F.update.message.as_("message"))
async def error_handler(event: ErrorEvent, message: Message):

    exception = event.exception

    if isinstance(exception, CallbackAnswerException):
        logger.critical("Exception for callback answer: \n %s", exception, exc_info=False)

    elif isinstance(exception, CallbackAnswerException):
        logger.critical("Exception for callback answer: \n %s", exception, exc_info=False)

    elif isinstance(exception, SceneException):
        logger.critical("Exception for scenes: \n %s", exception, exc_info=False)

    elif isinstance(exception, UnsupportedKeywordArgument):
        logger.critical("Exception raised when a keyword argument is passed as filter: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramRetryAfter):
        logger.critical("Exception raised when flood control exceeds: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramMigrateToChat):
        logger.critical("Exception raised when chat has been migrated to a supergroup: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramBadRequest):
        logger.critical("Exception raised when request is malformed: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramNotFound):
        logger.critical("Exception raised when chat, message, user, etc. not found: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramConflictError):
        logger.critical("Exception raised when bot token is already used by another application in polling mode: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramUnauthorizedError):
        logger.critical("Exception raised when bot token is invalid: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramForbiddenError):
        logger.critical("Exception raised when bot is kicked from chat or etc: \n %s", exception, exc_info=False)

    elif isinstance(exception, RestartingTelegram):
        logger.critical("Exception raised when Telegram server is restarting: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramEntityTooLarge):
        logger.critical("Exception raised when you are trying to send a file that is too large: \n %s", exception, exc_info=False)

    elif isinstance(exception, ClientDecodeError):
        logger.critical("Exception raised when client can't decode response. (Malformed response, etc.): \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramServerError):
        logger.critical("Exception raised when Telegram server returns 5xx error: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramNetworkError):
        logger.critical("Base exception for all Telegram network errors: \n %s", exception, exc_info=False)

    elif isinstance(exception, DetailedAiogramError):
        logger.critical("Base exception for all aiogram errors with detailed message: \n %s", exception, exc_info=False)

    elif isinstance(exception, TelegramAPIError):
        logger.critical("Base exception for all Telegram API errors: \n %s", exception, exc_info=False)

    elif isinstance(exception, AiogramError):
        logger.critical("Base exception for all aiogram errors: \n %s", exception, exc_info=False)

    else:
        logger.critical("Critical error caused by %s", exception, exc_info=False)