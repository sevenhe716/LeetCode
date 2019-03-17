import unittest

from common import test_by_reflect


class TestMicrosoft(unittest.TestCase):
    """Test m4323_microsoft.py"""

    def test_microsoft(self):
        commands = ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
        params = [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
        res = [None, 0, 0, 0, 0, 0, 0, 1]

        test_by_reflect(self, 'm4323_microsoft', commands, params, res)

        commands = ["TicTacToe", "move", "move", "move"]
        params = [[2], [0, 1, 1], [1, 1, 2], [1, 0, 1]]
        res = [None, 0, 0, 1]

        test_by_reflect(self, 'm4323_microsoft', commands, params, res)

if __name__ == '__main__':
    unittest.main()
