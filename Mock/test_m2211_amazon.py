import unittest

from Mock.m2211_amazon import Solution


class TestAmazon(unittest.TestCase):
    """Test m2211_amazon.py"""

    def test_amazon(self):
        s = Solution()

        self.assertEqual(True, s.isValid("()"))
        self.assertEqual(True, s.isValid("()[]{}"))
        self.assertEqual(False, s.isValid("(]"))
        self.assertEqual(False, s.isValid("([)]"))
        self.assertEqual(True, s.isValid("{[]}"))
        self.assertEqual(False, s.isValid("]"))


if __name__ == '__main__':
    unittest.main()
