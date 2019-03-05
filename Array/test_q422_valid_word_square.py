import unittest

from Array.q422_valid_word_square import Solution


class TestValidWordSquare(unittest.TestCase):
    """Test q422_valid_word_square.py"""

    def test_valid_word_square(self):
        s = Solution()

        self.assertEqual(True, s.validWordSquare([
            "abcd",
            "bnrt",
            "crmy",
            "dtye"
        ]))
        self.assertEqual(True, s.validWordSquare([
            "abcd",
            "bnrt",
            "crm",
            "dt"
        ]))
        self.assertEqual(False, s.validWordSquare([
            "ball",
            "area",
            "read",
            "lady"
        ]))


if __name__ == '__main__':
    unittest.main()
