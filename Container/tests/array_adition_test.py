import unittest

def arraysum(arr):
    return sum(arr)

class TestArraySum(unittest.TestCase):
    def test_arraysum_positive_integers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(arraysum(arr), 15)

    def test_arraysum_negative_integers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(arraysum(arr), -15)

    def test_arraysum_mixed_integers(self):
        arr = [-1, 2, -3, 4, -5]
        self.assertEqual(arraysum(arr), -3)

if __name__ == '__main__':
    unittest.main()
