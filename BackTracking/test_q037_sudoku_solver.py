import unittest

from BackTracking.q037_sudoku_solver import Solution


class TestSudokuSolver(unittest.TestCase):
    """Test q037_sudoku_solver.py"""

    def test_sudoku_solver(self):
        s = Solution()

        # self.assertEqual((0, 0), s.cal(0, 0))
        # self.assertEqual((0, 1), s.cal(0, 1))
        # self.assertEqual((0, 2), s.cal(0, 2))
        # self.assertEqual((1, 0), s.cal(0, 3))
        # self.assertEqual((1, 1), s.cal(0, 4))
        # self.assertEqual((1, 2), s.cal(0, 5))
        # self.assertEqual((2, 0), s.cal(0, 6))
        # self.assertEqual((2, 1), s.cal(0, 7))
        # self.assertEqual((2, 2), s.cal(0, 8))
        # self.assertEqual((0, 3), s.cal(1, 0))
        # self.assertEqual((0, 4), s.cal(1, 1))
        # self.assertEqual((0, 5), s.cal(1, 2))
        # self.assertEqual((1, 3), s.cal(1, 3))
        # self.assertEqual((1, 4), s.cal(1, 4))
        # self.assertEqual((1, 5), s.cal(1, 5))
        # self.assertEqual((2, 3), s.cal(1, 6))
        # self.assertEqual((2, 4), s.cal(1, 7))
        # self.assertEqual((2, 5), s.cal(1, 8))
        # self.assertEqual((3, 3), s.cal(4, 0))
        # self.assertEqual((3, 4), s.cal(4, 1))
        # self.assertEqual((3, 5), s.cal(4, 2))
        # self.assertEqual((4, 3), s.cal(4, 3))
        # self.assertEqual((4, 4), s.cal(4, 4))
        # self.assertEqual((4, 5), s.cal(4, 5))
        # self.assertEqual((5, 3), s.cal(4, 6))
        # self.assertEqual((5, 4), s.cal(4, 7))
        # self.assertEqual((5, 5), s.cal(4, 8))
        # self.assertEqual((3, 6), s.cal(5, 0))
        # self.assertEqual((3, 7), s.cal(5, 1))
        # self.assertEqual((3, 8), s.cal(5, 2))
        # self.assertEqual((4, 6), s.cal(5, 3))
        # self.assertEqual((4, 7), s.cal(5, 4))
        # self.assertEqual((4, 8), s.cal(5, 5))
        # self.assertEqual((5, 6), s.cal(5, 6))
        # self.assertEqual((5, 7), s.cal(5, 7))
        # self.assertEqual((5, 8), s.cal(5, 8))
        #
        # self.assertEqual(s.test(0, 0), (0, 0))
        # self.assertEqual(s.test(0, 1), (0, 1))
        # self.assertEqual(s.test(0, 2), (0, 2))
        # self.assertEqual(s.test(1, 0), (0, 3))
        # self.assertEqual(s.test(1, 1), (0, 4))
        # self.assertEqual(s.test(1, 2), (0, 5))
        # self.assertEqual(s.test(2, 0), (0, 6))
        # self.assertEqual(s.test(2, 1), (0, 7))
        # self.assertEqual(s.test(2, 2), (0, 8))
        # self.assertEqual(s.test(0, 3), (1, 0))
        # self.assertEqual(s.test(0, 4), (1, 1))
        # self.assertEqual(s.test(0, 5), (1, 2))
        # self.assertEqual(s.test(1, 3), (1, 3))
        # self.assertEqual(s.test(1, 4), (1, 4))
        # self.assertEqual(s.test(1, 5), (1, 5))
        # self.assertEqual(s.test(2, 3), (1, 6))
        # self.assertEqual(s.test(2, 4), (1, 7))
        # self.assertEqual(s.test(2, 5), (1, 8))
        # self.assertEqual(s.test(3, 3), (4, 0))
        # self.assertEqual(s.test(3, 4), (4, 1))
        # self.assertEqual(s.test(3, 5), (4, 2))
        # self.assertEqual(s.test(4, 3), (4, 3))
        # self.assertEqual(s.test(4, 4), (4, 4))
        # self.assertEqual(s.test(4, 5), (4, 5))
        # self.assertEqual(s.test(5, 3), (4, 6))
        # self.assertEqual(s.test(5, 4), (4, 7))
        # self.assertEqual(s.test(5, 5), (4, 8))
        # self.assertEqual(s.test(3, 6), (5, 0))
        # self.assertEqual(s.test(3, 7), (5, 1))
        # self.assertEqual(s.test(3, 8), (5, 2))
        # self.assertEqual(s.test(4, 6), (5, 3))
        # self.assertEqual(s.test(4, 7), (5, 4))
        # self.assertEqual(s.test(4, 8), (5, 5))
        # self.assertEqual(s.test(5, 6), (5, 6))
        # self.assertEqual(s.test(5, 7), (5, 7))
        # self.assertEqual(s.test(5, 8), (5, 8))

        # self.assertEqual((5, 7), s.test(*s.cal(1, 4)))

        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        s.solveSudoku(board)

        self.assertSequenceEqual([
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ], board)


if __name__ == '__main__':
    unittest.main()
