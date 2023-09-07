import unittest
from unittest.mock import MagicMock

import logic

class TestReadBooks(unittest.TestCase):
    def test_read_books(self):
        # Create a mock database connection
        conn = MagicMock()

        # Use the patch decorator to replace the database connection in the
        # my_module module with the mock connection
        with open("logic.conn", conn):
            # Call the read_books function
            result = logic.read_books()

            # Assert that the database connection was used correctly
            conn.execute.assert_called_once_with("select * from book limit 10;")
            conn.fetchall.assert_called_once()

            # Assert that the result is what we expect
            self.assertEqual(result, [{"id": 1, "title": "Book 1"}, {"id": 2, "title": "Book 2"}, ...])