import unittest

from common import test_by_reflect


class TestDesignTicTacToe(unittest.TestCase):
    """Test q348_design_tic_tac_toe.py"""

    def test_design_tic_tac_toe(self):
        commands = ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
        params = [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
        res = [None, 0, 0, 0, 0, 0, 0, 1]

        test_by_reflect(self, 'q348_design_tic_tac_toe', commands, params, res)

        commands = ["TicTacToe", "move", "move", "move"]
        params = [[2], [0, 1, 1], [1, 1, 2], [1, 0, 1]]
        res = [None, 0, 0, 1]

        test_by_reflect(self, 'q348_design_tic_tac_toe', commands, params, res)

if __name__ == '__main__':
    unittest.main()
