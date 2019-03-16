import unittest

from Mock.m1233_google import Solution
from Mock.m1233_google import Interval


class TestGoogle(unittest.TestCase):
    """Test m1233_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual([Interval(1, 6), Interval(8, 10), Interval(15, 18)], s.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
        self.assertEqual([Interval(1, 5)], s.merge([Interval(1, 4), Interval(4, 5)]))


if __name__ == '__main__':
    unittest.main()
