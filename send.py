from aiogram.types import Message
from utils.stickers import random_sticker, should_send_sticker

async def send_with_optional_sticker(message: Message, text: str, reply_markup=None):
    if should_send_sticker():
        sticker = random_sticker()
        if sticker:
            try:
                await message.answer_sticker(sticker)
            except:
                pass

    await message.answer(text, reply_markup=reply_markup)
