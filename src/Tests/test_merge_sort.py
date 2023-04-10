import unittest
from src.sorting.merge import mergeSort


class TestMergeSort(unittest.TestCase):
    def test_mergeSort(self):
        arr1 = [5, 2, 7, 1, 8, 10, 3]
        arr2 = [10, 8, 7, 5, 3, 2, 1]
        arr3 = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(mergeSort(arr1), [1, 2, 3, 5, 7, 8, 10])
        self.assertEqual(mergeSort(arr2), [1, 2, 3, 5, 7, 8, 10])
        self.assertEqual(mergeSort(arr3), [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
