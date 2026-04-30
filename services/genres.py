import random
from books_db import BOOKS_DB, GENRES

def get_random_book_by_genre(genre: str):
    authors = GENRES.get(genre, [])
    if not authors:
        return None

    author = random.choice(authors)
    books = BOOKS_DB.get(author, [])
    if not books:
        return None

    book = random.choice(books)
    return {"title": book["title"], "author": author}

def get_random_book_any():
    genre = random.choice(list(GENRES.keys()))
    return get_random_book_by_genre(genre)
