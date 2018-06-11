import unittest

from Array.q054_spiral_matrix import Solution


class TestSpiralMatrix(unittest.TestCase):
    """Test q054_spiral_matrix.py"""

    def test_spiral_matrix(self):
        s = Solution()

        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], s.spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))

        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], s.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]))

        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], s.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]))

        self.assertEqual([], s.spiralOrder([]))


if __name__ == '__main__':
    unittest.main()
