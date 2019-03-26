import unittest

from Mock.m2233_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2233_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], s.letterCombinations("23"))


if __name__ == '__main__':
    unittest.main()
