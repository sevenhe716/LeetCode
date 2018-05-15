import unittest

from HashTable.q003_longest_substring_without_repeating_characters import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    """Test q003_longest_substring_without_repeating_characters.py"""

    def test_lengthOfLongestSubstring(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(7, s.lengthOfLongestSubstring("wabwcdef"))
        self.assertEqual(1, s.lengthOfLongestSubstring("a"))
        self.assertEqual(0, s.lengthOfLongestSubstring(""))


if __name__ == '__main__':
    unittest.main()
