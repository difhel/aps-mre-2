import asyncio

from aiogram import Bot, Dispatcher
from bot import routers

dp = Dispatcher()


print("started")

async def main() -> None:
    bot = Bot("token")
    dp.include_router(routers.admin_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
