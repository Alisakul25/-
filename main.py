import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers.greetings import greetings_router

from handlers.start import start_router
from handlers.recommend import recommend_router
from handlers.random_book import random_router
from handlers.search_flibusta import search_router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

dp.include_router(greetings_router)
dp.include_router(start_router)
dp.include_router(recommend_router)
dp.include_router(random_router)
dp.include_router(search_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
