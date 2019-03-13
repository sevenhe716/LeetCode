import unittest

from Stack.q682_baseball_game import Solution


class TestBaseballGame(unittest.TestCase):
    """Test q682_baseball_game.py"""

    def test_baseball_game(self):
        s = Solution()

        self.assertEqual(30, s.calPoints(["5", "2", "C", "D", "+"]))
        self.assertEqual(27, s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))


if __name__ == '__main__':
    unittest.main()
