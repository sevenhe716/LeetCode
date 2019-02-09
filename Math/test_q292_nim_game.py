import unittest

from Math.q292_nim_game import Solution


class TestNimGame(unittest.TestCase):
    """Test q292_nim_game.py"""

    def test_nim_game(self):
        s = Solution()

        self.assertEqual(True, s.canWinNim(1))
        self.assertEqual(True, s.canWinNim(2))
        self.assertEqual(True, s.canWinNim(3))
        self.assertEqual(False, s.canWinNim(4))
        self.assertEqual(True, s.canWinNim(5))
        self.assertEqual(True, s.canWinNim(6))
        self.assertEqual(True, s.canWinNim(7))
        self.assertEqual(False, s.canWinNim(8))


if __name__ == '__main__':
    unittest.main()
