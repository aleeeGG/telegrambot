import asyncio

from aiogram import Bot, Dispatcher, Router
from handlers import include_routers

bot = Bot(token="7131010130:AAHdhUJSLwQjMJ0NAqJ4MkOjsu-N43RihJE")
dp = Dispatcher()
router = Router()

async def main():
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
