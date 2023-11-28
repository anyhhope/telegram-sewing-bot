import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import setup_routers
import psycopg2 
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_reader import config

conn = psycopg2.connect(
    host = config.host.get_secret_value(),
    database = config.database.get_secret_value(),
    user = config.user_base.get_secret_value(),
    password = config.password.get_secret_value()
)
redis = Redis(
  host = config.redis_host.get_secret_value(),
  port = config.redis_port.get_secret_value(),
  password = config.redis_password.get_secret_value()
)
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)


async def main() -> None:
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)   

    router = setup_routers()
    dp.include_router(router) 

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())