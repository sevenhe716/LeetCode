import unittest

from Temp.q889_spiral_matrix_iii import Solution


class TestSpiralMatrixIii(unittest.TestCase):
    """Test q889_spiral_matrix_iii.py"""

    def test_spiral_matrix_iii(self):
        s = Solution()

        # self.assertEqual([[0, 0], [0, 1], [0, 2], [0, 3]], s.spiralMatrixIII(1, 4, 0, 0))
        self.assertEqual(
            [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2],
             [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0],
             [3, 0], [2, 0], [1, 0], [0, 0]], s.spiralMatrixIII(5, 6, 1, 4))


if __name__ == '__main__':
    unittest.main()
