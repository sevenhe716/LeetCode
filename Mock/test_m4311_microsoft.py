import unittest

from Mock.m4311_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4311_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual("blue is sky the", s.reverseWords("the sky is blue"))
        self.assertEqual("world! hello", s.reverseWords("  hello world!  "))
        self.assertEqual("example good a", s.reverseWords("a good   example"))


if __name__ == '__main__':
    unittest.main()
