"""
    Doc https://t.me/Mvideo540bot
"""
import asyncio
from config import dp, bot
from router_processors import helpback, welcome, feedback, callme


async def main():
    """
    Awaits the start polling function with the bot.
    """
    dp.include_routers(welcome.router, feedback.router, callme.router,
                       helpback.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
