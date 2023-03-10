import unittest
from src.container.findValue import find_value


class TestFindValue(unittest.TestCase):
    def test_find_existing_value(self):
        arr = [1, 2, 3, 4, 5]
        val = 3
        self.assertEqual(find_value(arr, val), 2)

    def test_find_nonexisting_value(self):
        arr = [1, 2, 3, 4, 5]
        val = 6
        self.assertEqual(find_value(arr, val), -1)

    def test_find_duplicate_value(self):
        arr = [1, 2, 3, 3, 4, 5]
        val = 3
        self.assertEqual(find_value(arr, val), 2)

if __name__ == '__main__':
    unittest.main()