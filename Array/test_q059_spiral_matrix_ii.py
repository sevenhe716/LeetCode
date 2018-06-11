import unittest

from Array.q059_spiral_matrix_ii import Solution


class TestSpiralMatrixIi(unittest.TestCase):
    """Test q059_spiral_matrix_ii.py"""

    def test_spiral_matrix_ii(self):
        s = Solution()

        self.assertEqual([
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ], s.generateMatrix(3))

        self.assertEqual([[1, 2],
                          [4, 3]], s.generateMatrix(2))

        self.assertEqual([[1]], s.generateMatrix(1))

if __name__ == '__main__':
    unittest.main()
