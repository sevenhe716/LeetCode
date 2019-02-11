import unittest

from Array.q073_set_matrix_zeroes import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    """Test q073_set_matrix_zeroes.py"""

    def test_set_matrix_zeroes(self):
        s = Solution()

        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        s.setZeroes(matrix)
        self.assertEqual([
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ], matrix)

        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        s.setZeroes(matrix)
        self.assertEqual([
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ], matrix)


if __name__ == '__main__':
    unittest.main()
