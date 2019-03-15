import unittest

from BFS.q279_perfect_squares import Solution


class TestPerfectSquares(unittest.TestCase):
    """Test q279_perfect_squares.py"""

    def test_perfect_squares(self):
        s = Solution()

        self.assertEqual(3, s.numSquares(12))
        self.assertEqual(2, s.numSquares(13))


if __name__ == '__main__':
    unittest.main()
