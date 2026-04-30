from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Рекомендация книги по жанру")],
            [KeyboardButton(text="🎲 Случайная книга")],
            [KeyboardButton(text="🔎 Проверить наличие книги на Флибусте")],
        ],
        resize_keyboard=True
    )

def back_to_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔙 Вернуться в главное меню")]
        ],
        resize_keyboard=True
    )

def genres_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="триллер"), KeyboardButton(text="зарубежный детектив")],
            [KeyboardButton(text="фантастика"), KeyboardButton(text="хоррор")],
            [KeyboardButton(text="русский детектив"), KeyboardButton(text="русская классика")],
            [KeyboardButton(text="зарубежная классика"), KeyboardButton(text="современная проза")],
            [KeyboardButton(text="🔙 Вернуться в главное меню")]
        ],
        resize_keyboard=True
    )
