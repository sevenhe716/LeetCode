import unittest

from Math.q009_palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    """Test q009_palindrome_number.py"""

    def test_palindrome_number(self):
        s = Solution()
        self.assertEqual(True, s.isPalindrome(121))
        self.assertEqual(False, s.isPalindrome(-121))
        self.assertEqual(False, s.isPalindrome(10))
        self.assertEqual(True, s.isPalindrome(1221))
        self.assertEqual(True, s.isPalindrome(1))
        self.assertEqual(True, s.isPalindrome(22))
        self.assertEqual(True, s.isPalindrome(0))
        self.assertEqual(False, s.isPalindrome(2147483647))
        self.assertEqual(False, s.isPalindrome(-2147483648))


if __name__ == '__main__':
    unittest.main()
