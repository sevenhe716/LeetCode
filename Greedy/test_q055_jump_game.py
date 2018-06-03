import unittest

from Greedy.q055_jump_game import Solution


class TestJumpGame(unittest.TestCase):
    """Test q055_jump_game.py"""

    def test_jump_game(self):
        s = Solution()

        self.assertEqual(True, s.canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 4]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 6, 1, 0, 1, 0]))
        self.assertEqual(True, s.canJump([3, 2, 2, 0, 6, 1, 0, 1, 0]))
        self.assertEqual(True, s.canJump([0]))
        self.assertEqual(True, s.canJump([2, 0]))
        self.assertEqual(True, s.canJump([2, 0, 0]))
        self.assertEqual(True, s.canJump([1, 0]))
        self.assertEqual(False, s.canJump([1, 0, 0]))
        self.assertEqual(True, s.canJump([1, 2]))


if __name__ == '__main__':
    unittest.main()
