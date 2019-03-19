import unittest

from Mock.m3131_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m3131_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual("bab", s.longestPalindrome("babad"))
        self.assertEqual("bb", s.longestPalindrome("cbbd"))


if __name__ == '__main__':
    unittest.main()
