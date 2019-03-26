import unittest

from String.q151_reverse_words_in_a_string import Solution


class TestReverseWordsInAString(unittest.TestCase):
    """Test q151_reverse_words_in_a_string.py"""

    def test_reverse_words_in_a_string(self):
        s = Solution()

        self.assertEqual("blue is sky the", s.reverseWords("the sky is blue"))
        self.assertEqual("world! hello", s.reverseWords("  hello world!  "))
        self.assertEqual("example good a", s.reverseWords("a good   example"))


if __name__ == '__main__':
    unittest.main()
