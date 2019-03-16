import unittest

from Mock.m1231_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1231_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual([1], s.plusOne([0]))
        self.assertEqual([1, 3, 0], s.plusOne([1, 2, 9]))
        self.assertEqual([1, 0, 0], s.plusOne([9, 9]))
        self.assertEqual([4, 3, 2, 2], s.plusOne([4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
