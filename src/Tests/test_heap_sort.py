import unittest
from src.sorting.heap import heapSort

class TestHeapSort(unittest.TestCase):
    def test_heap_sort_with_sorted_list(self):
        sorted_list = [1, 2, 3, 4, 5, 6, 7]
       self.assertEqual(heapSort(sorted_list), [1, 2, 3, 4, 5, 6, 7])

    def test_heap_sort_with_reverse_sorted_list(self):
        reverse_sorted_list = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(heapSort(reverse_sorted_list), [1, 2, 3, 4, 5, 6, 7])

    def test_heap_sort_with_random_list(self):
        random_list = [3, 2, 5, 1, 4, 7, 6]
        self.assertEqual(heapSort(random_list), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
