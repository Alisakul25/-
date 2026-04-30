from aiogram import Router
from aiogram.types import Message
from services.genres import get_random_book_any
from services.flibusta_search import search_book_on_flibusta
from utils.keyboards import back_to_menu
from utils.send import send_with_optional_sticker

random_router = Router()

@random_router.message(lambda m: m.text == "🎲 Случайная книга")
async def random_book(message: Message):
    book = get_random_book_any()
    link = await search_book_on_flibusta(book["title"])

    await send_with_optional_sticker(
        message,
        f"📘 <b>{book['title']}</b>\n"
        f"✍️ {book['author']}\n"
        f"🔗 {link or 'Не найдено'}",
        reply_markup=back_to_menu()
    )
