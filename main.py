from library.operations import (
    add_book,
    delete_book,
    find_books,
    display_books,
    update_status,
)


def main():
    menu = """
    Система управления библиотекой:
    1. Добавить книгу
    2. Удалить книгу
    3. Найти книгу
    4. Отобразить все книги
    5. Изменить статус книги
    6. Выход
    """

    while True:
        print(menu)
        choice = input("Выберите опцию: ")

        match choice:
            case "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                add_book(title, author, year)
            case "2":
                book_id = int(input("Введите ID книги для удаления: "))
                delete_book(book_id)
            case "3":
                by = input("Искать по (title/author/year): ")
                query = input("Введите поисковый запрос: ")
                results = find_books(query, by)
                display_books(results)
            case "4":
                display_books()
            case "5":
                book_id = int(input("Введите ID книги: "))
                status = input("Введите новый статус (в наличии/выдана): ")
                update_status(book_id, status)
            case "6":
                print("Выход из программы...")
                break
            case _:
                print("Неверный выбор, попробуйте еще раз.")


if __name__ == "__main__":
    main()
