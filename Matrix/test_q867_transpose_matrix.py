import unittest

from Matrix.q867_transpose_matrix import Solution1


class TestTransposeMatrix(unittest.TestCase):
    """Test q867_transpose_matrix.py"""

    def test_transpose_matrix(self):
        s = Solution1()

        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual([[1, 4], [2, 5], [3, 6]], s.transpose([[1, 2, 3], [4, 5, 6]]))


if __name__ == '__main__':
    unittest.main()
