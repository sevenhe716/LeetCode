import unittest

from String.q157_read_n_characters_given_read4 import Solution


class TestReadNCharactersGivenRead4(unittest.TestCase):
    """Test q157_read_n_characters_given_read4.py"""

    def test_read_n_characters_given_read4(self):
        s = Solution()

        self.assertEqual(3, s.read("abc", 4))
        self.assertEqual(5, s.read("abcde", 5))
        self.assertEqual(12, s.read("abcdABCD1234", 12))
        self.assertEqual(5, s.read("leetcode", 5))


if __name__ == '__main__':
    unittest.main()
