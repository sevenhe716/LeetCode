import unittest

from String.q828_unique_letter_string import Solution2


class TestUniqueLetterString(unittest.TestCase):
    """Test q828_unique_letter_string.py"""

    def test_unique_letter_string(self):
        s = Solution2()

        self.assertEqual(21, s.uniqueLetterString('CABAB'))
        self.assertEqual(60, s.uniqueLetterString('DABCABE'))
        self.assertEqual(10, s.uniqueLetterString('ABC'))
        self.assertEqual(8, s.uniqueLetterString('ABA'))
        self.assertEqual(1, s.uniqueLetterString('A'))
        self.assertEqual(0, s.uniqueLetterString(''))


if __name__ == '__main__':
    unittest.main()
