import unittest

from Matrix.q240_search_a_2d_matrix_ii import Solution


class TestSearchA2DMatrixIi(unittest.TestCase):
    """Test q240_search_a_2d_matrix_ii.py"""

    def test_search_a_2d_matrix_ii(self):
        s = Solution()

        self.assertEqual(True, s.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5))

        self.assertEqual(False, s.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20))



if __name__ == '__main__':
    unittest.main()
