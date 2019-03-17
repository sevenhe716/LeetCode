import unittest

from Mock.m4231_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4231_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual("s'teL ekat edoCteeL tsetnoc", s.reverseWords("Let's take LeetCode contest"))


if __name__ == '__main__':
    unittest.main()
