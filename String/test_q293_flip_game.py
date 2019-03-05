import unittest

from String.q293_flip_game import Solution


class TestFlipGame(unittest.TestCase):
    """Test q293_flip_game.py"""

    def test_flip_game(self):
        s = Solution()

        self.assertEqual([
            "--++",
            "+--+",
            "++--"
        ], s.generatePossibleNextMoves("++++"))


if __name__ == '__main__':
    unittest.main()
