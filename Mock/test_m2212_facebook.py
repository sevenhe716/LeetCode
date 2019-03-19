import unittest

from Mock.m2212_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2212_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(True, s.validPalindrome("aba"))
        self.assertEqual(True, s.validPalindrome("abca"))


if __name__ == '__main__':
    unittest.main()
