import pytest
from unittest.mock import MagicMock, patch

from BookLibraryManagment.Customers import Customers

@pytest.fixture()
def cust_instance():
    return Customers()

def test_add_customer(cust_instance):
    with patch('BookLibraryManagment.Customers.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        cust_instance.add_customer("Madam Potato", "Waterloo", 98)

def test_show_all_customers(cust_instance):
    with patch('BookLibraryManagment.Customers.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        cust_instance.show_all_customers()

def test_find_customer(cust_instance):
    with patch('BookLibraryManagment.Customers.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        cust_instance.find_customer("Madam Potato")

def test_find_customer_BY_ID(cust_instance):
    with patch('BookLibraryManagment.Customers.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        cust_instance.find_customer_BY_ID(24)

def test_remove_customer(cust_instance):
    with patch('BookLibraryManagment.Customers.pyodbc.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        cust_instance.remove_customer(23)
