import unittest
from src.sorting.quickSort import quickSort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_with_positive_numbers(self):
        unsorted_list = [3, 1, 4, 2, 5]
        sorted_list = quickSort(unsorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

    def test_quick_sort_with_negative_numbers(self):
        unsorted_list = [-3, -1, -4, -2, -5]
        sorted_list = quickSort(unsorted_list)
        self.assertEqual(sorted_list, [-5, -4, -3, -2, -1])

    def test_quick_sort_with_mixed_numbers(self):
        unsorted_list = [-3, 1, 0, -2, 5]
        sorted_list = quickSort(unsorted_list)
        self.assertEqual(sorted_list, [-3, -2, 0, 1, 5])


if __name__ == '__main__':
    unittest.main()
