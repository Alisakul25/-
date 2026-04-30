from aiogram import Router
from aiogram.types import Message
from services.flibusta_search import search_book_on_flibusta
from utils.keyboards import back_to_menu

search_router = Router()

STATE = {}

@search_router.message(lambda m: m.text == "🔎 Проверить наличие книги на Флибусте")
async def ask_title(message: Message):
    STATE[message.from_user.id] = "awaiting"
    await message.answer("Напиши название книги:", reply_markup=back_to_menu())

@search_router.message()
async def do_search(message: Message):
    if STATE.get(message.from_user.id) != "awaiting":
        return

    STATE.pop(message.from_user.id)

    title = message.text.strip()
    link = await search_book_on_flibusta(title)

    if not link:
        return await message.answer("Не нашёл 😿", reply_markup=back_to_menu())

    await message.answer(f"📘 <b>{title}</b>\n🔗 {link}", reply_markup=back_to_menu())
