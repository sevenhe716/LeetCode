import unittest

from q004_median_of_two_sorted_arrays import Solution


class TestFindMedianSortedArrays(unittest.TestCase):
    """Test q004_median_of_two_sorted_arrays.py"""

    def test_findMedianSortedArrays(self):
        s = Solution()
        self.assertEqual(2.0, s.findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(2.0, s.findMedianSortedArrays([1, 2], [3]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 2, 5], [3]))
        self.assertEqual(2.0, s.findMedianSortedArrays([1, 2, 5], [2]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 3, 5], [2]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 2, 3], [5]))
        self.assertEqual(2.5, s.findMedianSortedArrays([0, 1, 2, 5, 7], [3]))
        self.assertEqual(2.0, s.findMedianSortedArrays([0, 1, 2, 5, 7], [2]))
        self.assertEqual(2.5, s.findMedianSortedArrays([0, 1, 3, 5, 7], [2]))
        self.assertEqual(2.5, s.findMedianSortedArrays([0, 1, 2, 3, 7], [5]))
        self.assertEqual(2.0, s.findMedianSortedArrays([1, 2], [3]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 2], [3, 4]))
        self.assertEqual(4.0, s.findMedianSortedArrays([4, 5], [3, 4, 5]))
        self.assertEqual(3.5, s.findMedianSortedArrays([1, 2], [3, 4, 5, 6]))
        self.assertEqual(3.0, s.findMedianSortedArrays([1, 2, 3], [3, 4, 5]))
        self.assertEqual(3.0, s.findMedianSortedArrays([3], [1, 2, 3, 4, 5]))
        self.assertEqual(1.0, s.findMedianSortedArrays([1, 2], [1, 1]))
        self.assertEqual(1.0, s.findMedianSortedArrays([1, 1], [1, 2]))
        self.assertEqual(1.0, s.findMedianSortedArrays([1, 1, 2], [1, 1]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 4], [2, 3]))
        self.assertEqual(1.5, s.findMedianSortedArrays([1, 2], [0, 1, 5, 6]))
        self.assertEqual(2.5, s.findMedianSortedArrays([2, 3], [0, 1, 5, 6]))
        self.assertEqual(3.5, s.findMedianSortedArrays([1, 2, 5], [3, 4, 6]))


if __name__ == '__main__':
    unittest.main()
