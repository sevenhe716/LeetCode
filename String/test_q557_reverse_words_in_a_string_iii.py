import unittest

from String.q557_reverse_words_in_a_string_iii import Solution


class TestReverseWordsInAStringIii(unittest.TestCase):
    """Test q557_reverse_words_in_a_string_iii.py"""

    def test_reverse_words_in_a_string_iii(self):
        s = Solution()

        self.assertEqual("s'teL ekat edoCteeL tsetnoc", s.reverseWords("Let's take LeetCode contest"))


if __name__ == '__main__':
    unittest.main()
