import unittest

from SlidingWindow.q159_longest_substring_with_at_most_two_distinct_characters import Solution


class TestLongestSubstringWithAtMostTwoDistinctCharacters(unittest.TestCase):
    """Test q159_longest_substring_with_at_most_two_distinct_characters.py"""

    def test_longest_substring_with_at_most_two_distinct_characters(self):
        s = Solution()

        self.assertEqual(3, s.lengthOfLongestSubstringTwoDistinct("eceba"))
        self.assertEqual(5, s.lengthOfLongestSubstringTwoDistinct("ccaabbb"))


if __name__ == '__main__':
    unittest.main()
