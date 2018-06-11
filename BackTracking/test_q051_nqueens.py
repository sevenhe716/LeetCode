import unittest

from BackTracking.q051_nqueens import Solution


class TestNqueens(unittest.TestCase):
    """Test q051_nqueens.py"""

    def test_nqueens(self):
        s = Solution()

        self.assertEqual(sorted([[".Q..",
                                  "...Q",
                                  "Q...",
                                  "..Q."],
                                 ["..Q.",
                                  "Q...",
                                  "...Q",
                                  ".Q.."]]), sorted(s.solveNQueens(4)))

        if __name__ == '__main__':
            unittest.main()
