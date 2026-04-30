import aiohttp
import urllib.parse

# Список зеркал — от самых стабильных к менее стабильным
FLIBUSTA_MIRRORS = [
    "https://flibusta.site",
    "https://flibusta.one",
    "https://flibusta.su",
    "https://flibusta.is",
]

async def search_book_on_flibusta(title: str):
    """
    Ищет книгу на Флибусте, перебирая зеркала.
    Возвращает ссылку на книгу или None.
    """

    query = urllib.parse.quote(title)

    for base in FLIBUSTA_MIRRORS:
        url = f"{base}/booksearch?ask={query}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as resp:
                    if resp.status != 200:
                        continue

                    html = await resp.text()

        except Exception:
            # Если зеркало не отвечает — пробуем следующее
            continue

        # Парсим HTML построчно
        for line in html.splitlines():
            if 'href="/b/' in line:
                try:
                    part = line.split('href="')[1].split('"')[0]
                    return base + part
                except Exception:
                    continue

    # Если ни одно зеркало не дало результата
    return None
