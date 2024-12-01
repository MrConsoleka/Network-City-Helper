from typing import Any, Awaitable, Callable, Dict
from datetime import datetime, timedelta

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery
from cachetools import TTLCache


class ThrottlingMiddlewareButton(BaseMiddleware):
    def __init__(self, time_limit_s: int = 2) -> None:
        self.limit = TTLCache(maxsize=10000, ttl=time_limit_s)
        self.time_limit = time_limit_s

    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any],
    ) -> Any:
        current_time = datetime.now()

        if event.from_user.id in self.limit:
            expire_time = self.limit[event.from_user.id]
            remaining_time = (expire_time - current_time).total_seconds()

            if remaining_time > 0:
                await event.answer(
                    f"Пожалуйста, подождите {remaining_time:.1f} секунд!"
                )
                return

        self.limit[event.from_user.id] = current_time + timedelta(seconds=self.time_limit)
        return await handler(event, data)
