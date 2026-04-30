import aiohttp
import urllib.parse

BASE_URL = "https://flibusta.is"

async def search_book_on_flibusta(title: str):
    query = urllib.parse.quote(title)
    url = f"{BASE_URL}/booksearch?ask={query}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status != 200:
                    return None
                html = await resp.text()
    except:
        return None

    for line in html.splitlines():
        if 'href="/b/' in line:
            try:
                part = line.split('href="')[1].split('"')[0]
                return BASE_URL + part
            except:
                continue

    return None
