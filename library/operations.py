from typing import List, Dict
from library.storage import load_books, save_books
from library.models import Book


def add_book(title: str, author: str, year: int):
    """Добавляет книгу в библиотеку."""
    try:
        books = load_books()
        new_book = Book(title, author, year)
        books.append(new_book.to_dict())
        save_books(books)
        print(f'Книга "{title}" успешно добавлена c ID {new_book.id}.')
    except Exception as e:
        print(f"Ошибка при добавлении книги: {e}")


def delete_book(book_id: int):
    """Удаляет книгу из библиотеки (по ID)."""
    try:
        books = load_books()
        if any(book["id"] == book_id for book in books):
            books = [book for book in books if book["id"] != book_id]
            save_books(books)
            print(f"Книга c ID {book_id} успешно удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при удалении книги: {e}")


def find_books(query: str, by: str = "title") -> List[Dict]:
    """Находит книги в библиотеке по названию, автору или году."""
    try:
        books = load_books()
        found_books = [book for book in books if query.lower() in str(book[by]).lower()]
        if not found_books:
            print(f"По запросу '{query}' книги не найдены.")
        return found_books
    except KeyError:
        print(f"Некорректное поле для поиска: {by}")
        return []
    except Exception as e:
        print(f"Ошибка при поиске книг: {e}")
        return []


def display_books(books: List[Dict] = None):
    """Выводит книги из библиотеки."""
    try:
        if books is None:
            books = load_books()
        if not books:
            print("В библиотеке нет книг.")
        else:
            for book in books:
                print(
                    f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}"
                )
    except Exception as e:
        print(f"Ошибка при выводе книг: {e}")


def update_status(book_id: int, status: str):
    """Обновляет статус книги (по ID)."""
    try:
        books = load_books()
        for book in books:
            if book["id"] == book_id:
                book["status"] = status
                save_books(books)
                print(f'Статус книги c ID {book_id} успешно обновлен на "{status}".')
                return
        print(f"Книга с ID {book_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при обновлении статуса книги: {e}")
