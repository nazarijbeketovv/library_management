import os
import json
from typing import List, Dict

BOOKS_FILE = "books.json"


def load_books() -> List[Dict]:
    """Загрузка книг из JSON файла."""
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_books(books: List[Dict]):
    """Сохранение книг в JSON файл."""
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
