import json
import os
from typing import List, Dict

BOOKS_FILE = "books.json"


def load_books() -> List[Dict]:
    """Загружает книги из JSON файла."""
    try:
        if os.path.exists(BOOKS_FILE):
            if os.path.getsize(BOOKS_FILE) > 0:
                with open(BOOKS_FILE, "r", encoding="utf-8") as file:
                    return json.load(file)
            else:
                print("Файл books.json пуст. Инициализация пустым списком.")
                save_books([])  # Инициализация пустым списком
                return []
        return []
    except json.JSONDecodeError:
        print(
            "Ошибка: файл books.json поврежден или пуст. Загружаем пустую библиотеку."
        )
        return []
    except Exception as e:
        print(f"Ошибка при загрузке книг: {e}")
        return []


def save_books(books: List[Dict]):
    """Сохраняет книги в JSON файл."""
    try:
        with open(BOOKS_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении книг: {e}")
