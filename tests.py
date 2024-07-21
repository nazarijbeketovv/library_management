import unittest
from unittest.mock import patch
from library.operations import (
    add_book,
    delete_book,
    find_books,
    display_books,
    update_status,
)


class TestLibraryFunctions(unittest.TestCase):

    @patch("library.operations.load_books")
    @patch("library.operations.save_books")
    @patch("library.models.Book.generate_id", return_value=1)
    def test_add_book(self, mock_generate_id, mock_save_books, mock_load_books):
        mock_load_books.return_value = []
        mock_save_books.return_value = None

        add_book("Test Title", "Test Author", 2024)

        mock_load_books.assert_called_once()
        mock_save_books.assert_called_once()
        saved_books = mock_save_books.call_args[0][0]
        self.assertEqual(len(saved_books), 1)
        self.assertEqual(saved_books[0]["title"], "Test Title")
        self.assertEqual(saved_books[0]["author"], "Test Author")
        self.assertEqual(saved_books[0]["year"], 2024)
        self.assertEqual(saved_books[0]["status"], "в наличии")
        self.assertEqual(saved_books[0]["id"], 1)

    @patch("library.operations.load_books")
    @patch("library.operations.save_books")
    def test_delete_book(self, mock_save_books, mock_load_books):
        mock_load_books.return_value = [
            {"id": 1, "title": "Test Book", "author": "Test Author", "year": 2024}
        ]
        mock_save_books.return_value = None

        delete_book(1)

        mock_load_books.assert_called_once()
        mock_save_books.assert_called_once()
        saved_books = mock_save_books.call_args[0][0]
        self.assertEqual(len(saved_books), 0)

    @patch("library.operations.load_books")
    def test_find_books_by_title(self, mock_load_books):
        mock_load_books.return_value = [
            {"id": 1, "title": "Test Book", "author": "Test Author", "year": 2024},
            {
                "id": 2,
                "title": "Another Book",
                "author": "Another Author",
                "year": 2023,
            },
        ]

        found_books = find_books("Test Book", by="title")

        mock_load_books.assert_called_once()
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0]["title"], "Test Book")

    @patch("library.operations.load_books")
    def test_find_books_by_author(self, mock_load_books):
        mock_load_books.return_value = [
            {"id": 1, "title": "Test Book", "author": "Test Author", "year": 2024},
            {
                "id": 2,
                "title": "Another Book",
                "author": "Another Author",
                "year": 2023,
            },
        ]

        found_books = find_books("Test Author", by="author")

        mock_load_books.assert_called_once()
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0]["author"], "Test Author")

    @patch("library.operations.load_books")
    @patch("library.operations.save_books")
    def test_update_status(self, mock_save_books, mock_load_books):
        mock_load_books.return_value = [
            {
                "id": 1,
                "title": "Test Book",
                "author": "Test Author",
                "year": 2024,
                "status": "в наличии",
            }
        ]
        mock_save_books.return_value = None

        update_status(1, "выдано")

        mock_load_books.assert_called_once()
        mock_save_books.assert_called_once()
        saved_books = mock_save_books.call_args[0][0]
        self.assertEqual(saved_books[0]["status"], "выдано")

    @patch("library.operations.load_books")
    def test_display_books(self, mock_load_books):
        mock_load_books.return_value = [
            {
                "id": 1,
                "title": "Test Book",
                "author": "Test Author",
                "year": 2024,
                "status": "в наличии",
            }
        ]

        with patch("builtins.print") as mock_print:
            display_books()
            mock_print.assert_any_call(
                "ID: 1, Название: Test Book, Автор: Test Author, Год: 2024, Статус: в наличии"
            )


if __name__ == "__main__":
    unittest.main()
