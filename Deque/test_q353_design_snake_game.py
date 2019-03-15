import unittest

from common import test_by_reflect


class TestDesignSnakeGame(unittest.TestCase):
    """Test q353_design_snake_game.py"""

    def test_design_snake_game(self):
        commands = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
        params = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
        res = [None, 0, 0, 1, 1, 2, -1]
        test_by_reflect(self, 'q353_design_snake_game', commands, params, res)

        commands = ["SnakeGame", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move",
                    "move"]
        params = [[3, 3, [[2, 0], [0, 0], [0, 2], [2, 2]]], ["D"], ["D"], ["R"], ["U"], ["U"], ["L"], ["D"], ["R"],
                  ["R"], ["U"],
                  ["L"], ["D"]]
        res = [None, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
        test_by_reflect(self, 'q353_design_snake_game', commands, params, res)


if __name__ == '__main__':
    unittest.main()
