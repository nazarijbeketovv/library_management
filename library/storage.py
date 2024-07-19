import json
import os
from typing import List, Dict

BOOKS_FILE = "books.json"


def load_books() -> List[Dict]:
    """Загружаем книги из JSON файла"""
    if os.path.exists(BOOKS_FILE):
        if os.path.getsize(BOOKS_FILE) > 0:
            with open(BOOKS_FILE, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print(
                        "Ошибка: файл books.json поврежден или пуст. Загружаем пустую библиотеку."
                    )
                    return []
        else:
            print("Файл books.json пуст. Инициализация пустым списком.")
            save_books([])  # Инициализация пустым списком
            return []
    return []


def save_books(books: List[Dict]):
    """Cохраняем книги в JSON файл"""
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
