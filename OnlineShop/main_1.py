import asyncio
from aiogram import Dispatcher, Bot
from app.handlers import dp

bot = Bot(token='7417222730:AAFOHtp6q3tohsszNwpBSQ_PjSO7rtBAA7Y')
router = Dispatcher(bot=bot)


async def main():
    router.include_router(dp)
    await router.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
