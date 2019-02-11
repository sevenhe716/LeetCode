import unittest

from BinarySearch.q074_search_a_2d_matrix import Solution


class TestSearchA2DMatrix(unittest.TestCase):
    """Test q074_search_a_2d_matrix.py"""

    def test_search_a_2d_matrix(self):
        s = Solution()

        self.assertEqual(True, s.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 3))
        self.assertEqual(False, s.searchMatrix([
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 13))
        self.assertEqual(False, s.searchMatrix([[1, 1]], 2))


if __name__ == '__main__':
    unittest.main()
