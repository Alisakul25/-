import random
from aiogram import Router
from aiogram.types import Message
from utils.keyboards import main_menu

greetings_router = Router()

GREETINGS = [
    "привет",
    "здравствуй",
    "доброе утро",
    "добрый день",
    "добрый вечер",
    "хай",
    "хелло",
    "нихау",
    "ку",
    "салам",
    "прив",
    "Привет, Гоша",
    "Привет, Георгий",
    "Привет",
    "Нихау, Гоша",

]

ALISA_ID = 1737343332  # твой ID

# Рандомные приветствия Гоши
CAT_GREETINGS = [
    "Мяу! Рад тебя видеть! 🐾",
    "Мур-мур! Гоша на месте! 😺",
    "Привет! Я Гоша — книжный кот! 📚🐈",
    "Мяу! Что читаем сегодня? 📖",
    "Гоша тут! Готов подобрать книгу! 🐾",
    "Мур! Как настроение? 😼",
    "Мяу-мяу! Давай выберем что-нибудь интересное! 📚",
]

@greetings_router.message(lambda m: m.text and m.text.lower() in GREETINGS)
async def greet_user(message: Message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    # Персональное приветствие для Алисы
    if user_id == ALISA_ID:
        text = "Привет, Алиса! Чем могу помочь?"
    else:
        # Случайное приветствие Гоши
        text = random.choice(CAT_GREETINGS)

    await message.answer(text, reply_markup=main_menu())
