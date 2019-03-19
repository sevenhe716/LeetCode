import unittest

from Mock.m2211_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2211_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(True, s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(False, s.isPalindrome("race a car"))
        self.assertEqual(False, s.isPalindrome("0P"))


if __name__ == '__main__':
    unittest.main()
