import unittest

from Temp.q877_stone_game import Solution


class TestStoneGame(unittest.TestCase):
    """Test q877_stone_game.py"""

    def test_stone_game(self):
        s = Solution()

        self.assertEqual(True, s.stoneGame([5, 3, 4, 5]))
        self.assertEqual(True, s.stoneGame([5, 4, 2, 3, 4, 5]))
        self.assertEqual(True, s.stoneGame([4, 4, 3, 3, 4, 5]))
        self.assertEqual(True, s.stoneGame([1, 6, 6, 9, 8, 10, 5, 4]))
        self.assertEqual(True, s.stoneGame([3, 7, 2, 3]))
        self.assertEqual(True, s.stoneGame([3, 2, 1, 3]))
        self.assertEqual(True, s.stoneGame([3, 1, 2, 3]))
        self.assertEqual(True, s.stoneGame([3, 2, 10, 4]))
        self.assertEqual(True, s.stoneGame([6, 9, 4, 3, 9, 8]))


if __name__ == '__main__':
    unittest.main()
