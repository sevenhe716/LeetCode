import unittest

from Mock.m2131_facebook import Solution


class TestFacebook(unittest.TestCase):
    """Test m2131_facebook.py"""

    def test_facebook(self):
        s = Solution()

        self.assertEqual(3, s.romanToInt("III"))
        self.assertEqual(4, s.romanToInt("IV"))
        self.assertEqual(9, s.romanToInt("IX"))
        self.assertEqual(58, s.romanToInt("LVIII"))
        self.assertEqual(1994, s.romanToInt("MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
