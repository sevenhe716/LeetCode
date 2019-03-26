import unittest

from String.q680_valid_palindrome_ii import Solution


class TestValidPalindromeIi(unittest.TestCase):
    """Test q680_valid_palindrome_ii.py"""

    def test_valid_palindrome_ii(self):
        s = Solution()

        self.assertEqual(True, s.validPalindrome("aba"))
        self.assertEqual(True, s.validPalindrome("abca"))


if __name__ == '__main__':
    unittest.main()
