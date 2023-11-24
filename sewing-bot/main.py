import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import setup_routers

from config_reader import config

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)   

    router = setup_routers()
    dp.include_router(router) 

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())