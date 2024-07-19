from typing import List, Dict
from book import Book
from utils import load_books, save_books


def add_book(title: str, author: str, year: int):
    """Добавляет книгу в библиотеку."""
    books = load_books()
    new_book = Book(title, author, year)
    books.append(new_book.to_dict())
    save_books(books)
    print(f'Книга "{title}" успешно добавлена с ID {new_book.id}.')


def delete_book(book_id: int):
    """Удаляет книгу из библиотеки(по ID)."""
    books = load_books()
    books = [book for book in books if book["id"] != book_id]
    save_books(books)
    print(f"Книга с ID {book_id} успешно удалена.")


def find_books(query: str, by: str = "title") -> List[Dict]:
    """Найти книги в библиотеке по названию, автору или году."""
    books = load_books()
    return [book for book in books if query.lower() in str(book[by]).lower()]


def display_books(books: List[Dict] = None):
    """Вывести книги из библиотеки."""
    if books is None:
        books = load_books()
    for book in books:
        print(
            f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}"
        )


def update_status(book_id: int, status: str):
    """Обновляет статус книги(по ID)."""
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book["status"] = status
            break
    save_books(books)
    print(f'Статус книги с ID {book_id} успешно обновлен на "{status}".')
