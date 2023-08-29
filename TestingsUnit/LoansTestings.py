import pytest
from unittest.mock import MagicMock, patch

from BookLibraryManagment.Loans import Loans

@pytest.fixture()
def loan_instance():
    return Loans()

def test_loan_book(loan_instance):
    with patch('BookLibraryManagment.Loans.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        loan_instance.loan_book(1,2)

def test_return_book(loan_instance):
    with patch('BookLibraryManagment.Loans.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        loan_instance.return_book(2)

def test_show_all_loans(loan_instance):
    with patch('BookLibraryManagment.Loans.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        loan_instance.show_all_loans()

def test_LATE(loan_instance):
    with patch('BookLibraryManagment.Loans.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        loan_instance.LATE()
