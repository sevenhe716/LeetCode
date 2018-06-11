import unittest

from String.q848_shifting_letters import Solution


class TestShiftingLetters(unittest.TestCase):
    """Test q848_shifting_letters.py"""

    def test_shifting_letters(self):
        s = Solution()

        self.assertEqual("rpl", s.shiftingLetters("abc", [3, 5, 9]))
        self.assertEqual("deahllnr", s.shiftingLetters("gdhbjaph", [74, 34, 65, 30, 43, 91, 14, 10]))
        self.assertEqual("b", s.shiftingLetters("a", [1]))


if __name__ == '__main__':
    unittest.main()
