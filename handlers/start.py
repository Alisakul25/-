from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from utils.keyboards import main_menu

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет, мой дорогой друг! Я книжный кот Гоша и я помогу тебе найти самую интересную историю 📚\nВыбирай, что делаем:",
        reply_markup=main_menu()
    )

@start_router.message(lambda m: m.text == "🔙 Вернуться в главное меню")
async def back_to_main(message: Message):
    await message.answer(
        "Главное меню:",
        reply_markup=main_menu()
    )
