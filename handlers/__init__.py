"""init"""
from aiogram import Dispatcher

from handlers import anketa, start


def include_routers(dp: Dispatcher):
    """обработчик модулей"""
    dp.include_routers(
        start.router,
        anketa.router)
