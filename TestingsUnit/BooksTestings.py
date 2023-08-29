import pytest
from unittest.mock import MagicMock, patch

from BookLibraryManagment.Books import Books

@pytest.fixture()
def book_instance():
    return Books()

def test_add_book(book_instance):
    with patch('BookLibraryManagment.Books.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        book_instance.add_book("This is going to Hurt","Adam Kay",2017,2)

def test_show_all_books(book_instance):
    with patch('BookLibraryManagment.Books.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        book_instance.show_all_books()

def test_find_book(book_instance):
    with patch('BookLibraryManagment.Books.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        book_instance.find_book("This is going to Hurt")

def test_find_book_BY_ID(book_instance):
    with patch('BookLibraryManagment.Books.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        book_instance.find_book_BY_ID(5)

def test_remove_book(book_instance):
    with patch('BookLibraryManagment.Books.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        book_instance.remove_book(5)

