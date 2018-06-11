import unittest

from Array.q056_merge_intervals import Solution
from common import Interval

class TestMergeIntervals(unittest.TestCase):
    """Test q056_merge_intervals.py"""

    def test_merge_intervals(self):
        s = Solution()

        self.assertEqual([[1, 6], [8, 10], [15, 18]], s.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
        self.assertEqual([[1, 5]], s.merge([Interval(1, 4), Interval(4, 5)]))


if __name__ == '__main__':
    unittest.main()
