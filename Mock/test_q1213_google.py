import unittest

from Mock.q1213_google import Solution


class TestGoogle(unittest.TestCase):
    """Test q1213_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual("<b>abc</b>xyz<b>123</b>", s.addBoldTag("abcxyz123", ["abc","123"]))
        self.assertEqual("<b>aaabbc</b>c", s.addBoldTag("aaabbcc", ["aaa","aab","bc"]))


if __name__ == '__main__':
    unittest.main()
