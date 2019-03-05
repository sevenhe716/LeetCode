import unittest

from String.q408_valid_word_abbreviation import Solution


class TestValidWordAbbreviation(unittest.TestCase):
    """Test q408_valid_word_abbreviation.py"""

    def test_valid_word_abbreviation(self):
        s = Solution()

        self.assertEqual(True, s.validWordAbbreviation('internationalization', 'i12iz4n'))
        self.assertEqual(False, s.validWordAbbreviation('apple', 'a2e'))
        self.assertEqual(False, s.validWordAbbreviation('apple', 'a2'))
        self.assertEqual(False, s.validWordAbbreviation('apple', 'a4e'))
        self.assertEqual(False, s.validWordAbbreviation('a', '2'))
        self.assertEqual(False, s.validWordAbbreviation('a', '01'))


if __name__ == '__main__':
    unittest.main()
