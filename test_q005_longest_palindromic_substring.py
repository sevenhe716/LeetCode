import unittest

from q005_longest_palindromic_substring import Solution


class TestLongestPalindrome(unittest.TestCase):
    """Test q005_longest_palindromic_substring.py"""

    def test_longestPalindrome(self):
        s = Solution()
        self.assertEqual("bab", s.longestPalindrome("babad"))
        self.assertEqual("bb", s.longestPalindrome("cbbd"))
        self.assertEqual("aa", s.longestPalindrome("aabc"))
        self.assertEqual("a", s.longestPalindrome("abc"))
        self.assertEqual("abfeefba", s.longestPalindrome("adbabfeefba"))
        self.assertEqual("aaaa", s.longestPalindrome("aaaa"))
        self.assertEqual("aaa", s.longestPalindrome("aaaca"))
        self.assertEqual("a", s.longestPalindrome("a"))
        self.assertEqual("", s.longestPalindrome(""))
        self.assertEqual("a", s.longestPalindrome("abcdasdfghjkldcba"))


if __name__ == '__main__':
    unittest.main()
