import random


STICKERS = [
    # сюда вставь реальные file_id стикеров котов
    "CAACAgIAAxkBAAIBGmnxbeOmJYKXE_7RrH3D0Xl4uRb2AAJPowADnoFLqX0vM9qsskI7BA",
    "CAACAgIAAxkBAAIBIGnxcJ1R_mERMAKlwIjI0ZI8v1WNAAI8sgACPhGISzFtGi1yUZzZOwQ",

]


def random_sticker():
    if not STICKERS:
        return None
    return random.choice(STICKERS)

def should_send_sticker(probability: float = 0.7) -> bool:
    return random.random() < probability
