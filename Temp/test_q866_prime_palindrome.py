import unittest

from Temp.q866_prime_palindrome import Solution1


class TestPrimePalindrome(unittest.TestCase):
    """Test q866_prime_palindrome.py"""

    def test_prime_palindrome(self):
        s = Solution1()

        self.assertEqual(2, s.primePalindrome(0))
        self.assertEqual(2, s.primePalindrome(-6))
        self.assertEqual(7, s.primePalindrome(6))
        self.assertEqual(7, s.primePalindrome(7))
        self.assertEqual(11, s.primePalindrome(8))
        self.assertEqual(101, s.primePalindrome(13))
        self.assertEqual(100030001, s.primePalindrome(9989900))


if __name__ == '__main__':
    unittest.main()
