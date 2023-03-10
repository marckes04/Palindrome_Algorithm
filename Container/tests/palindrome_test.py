import unittest
from src.container.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_multiple_word_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello world"))

if __name__ == '__main__':
    unittest.main()