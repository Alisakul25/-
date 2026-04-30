import uuid
from aiogram import Router
from aiogram.types import Message
from services.genres import get_random_book_by_genre
from services.flibusta_search import search_book_on_flibusta
from utils.keyboards import genres_keyboard, back_to_menu
from utils.send import send_with_optional_sticker

recommend_router = Router()

GENRE_BUTTONS = [
    "триллер",
    "зарубежный детектив",
    "фантастика",
    "хоррор",
    "русский детектив",
    "русская классика",
    "зарубежная классика",
    "современная проза",
]

@recommend_router.message(lambda m: m.text == "📚 Рекомендация книги по жанру")
async def choose_genre(message: Message):
    await message.answer("Выбери жанр:", reply_markup=genres_keyboard())

@recommend_router.message(lambda m: m.text in GENRE_BUTTONS)
async def recommend_for_genre(message: Message):
    book = get_random_book_by_genre(message.text)

    if not book:
        return await message.answer("Не нашёл книгу 😿", reply_markup=back_to_menu())

    link = await search_book_on_flibusta(book["title"])

    await send_with_optional_sticker(
        message,
        f"📘 <b>{book['title']}</b>\n"
        f"✍️ {book['author']}\n"
        f"🔗 {link or 'Не найдено'}",
        reply_markup=back_to_menu()
    )
