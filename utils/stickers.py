import random


STICKERS = [
    # сюда вставь реальные file_id стикеров котов
    "CAACAgIAAxkBAAIBGmnxbeOmJYKXE_7RrH3D0Xl4uRb2AAJPowADnoFLqX0vM9qsskI7BA",
    "CAACAgIAAxkBAAERLcRp_XZOBcarVEkV4kcO5llrHLD0sAACApEAAgfi8EsLCNFcpOU-cDsE",
    "CAACAgIAAxkBAAERLcZp_Xo8aM2S82Gf9DrVbU-PXxrV8QACGJEAAgfi8EtLbz9obFmxDDsE",
    "CAACAgIAAxkBAAERLcpp_Xrs_EkMvjc5Ep9jpbuGwdq9RQACI5EAAgfi8EukhXiF9m0GvjsE",
    "CAACAgIAAxkBAAERLc9p_X1S-vgB0Z03b7kVD2oDraERDAACPJEAAgfi8EtYi_HPipPDbDsE",
    ]


def random_sticker():
    if not STICKERS:
        return None
    return random.choice(STICKERS)

def should_send_sticker(probability: float = 0.7) -> bool:
    return random.random() < probability
