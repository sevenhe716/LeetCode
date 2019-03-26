import unittest

from Matrix.q766_toeplitz_matrix import Solution


class TestToeplitzMatrix(unittest.TestCase):
    """Test q766_toeplitz_matrix.py"""

    def test_toeplitz_matrix(self):
        s = Solution()

        self.assertEqual(True, s.isToeplitzMatrix(matrix=[
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 2]
        ]))
        self.assertEqual(False, s.isToeplitzMatrix(matrix=[
            [1, 2],
            [2, 2]
        ]))


if __name__ == '__main__':
    unittest.main()
