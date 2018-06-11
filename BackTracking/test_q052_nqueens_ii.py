import unittest

from BackTracking.q052_nqueens_ii import Solution


class TestNqueensIi(unittest.TestCase):
    """Test q052_nqueens_ii.py"""

    def test_nqueens_ii(self):
        s = Solution()

        self.assertEqual(2, s.totalNQueens(4))


if __name__ == '__main__':
    unittest.main()
