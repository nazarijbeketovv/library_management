import os
import json
from typing import Dict

BOOKS_FILE = "books.json"


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    @staticmethod
    def generate_id() -> int:
        """Генератор уникального ID для книги."""
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r", encoding="utf-8") as file:
                books = json.load(file)
                if books:
                    return max(book["id"] for book in books) + 1
        return 1

    def to_dict(self) -> Dict:
        """Конвертер объекта книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }
