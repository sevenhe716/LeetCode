import unittest

from String.q125_valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    """Test q125_valid_palindrome.py"""

    def test_valid_palindrome(self):
        s = Solution()

        self.assertEqual(True, s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(False, s.isPalindrome("race a car"))
        self.assertEqual(False, s.isPalindrome("0P"))


if __name__ == '__main__':
    unittest.main()
