import unittest

from Array.q057_insert_interval import Solution
from common import Interval


class TestInsertInterval(unittest.TestCase):
    """Test q057_insert_interval.py"""

    def test_insert_interval(self):
        s = Solution()

        self.assertEqual([[-2, 0], [1, 5], [6, 9]], s.insert([Interval(-2, 0), Interval(3, 5), Interval(6, 9)], Interval(1, 4)))
        self.assertEqual([[1, 5], [6, 9]], s.insert([Interval(3, 5), Interval(6, 9)], Interval(1, 4)))
        self.assertEqual([[-2, 0], [1, 2], [3, 5], [6, 9]], s.insert([Interval(-2, 0), Interval(3, 5), Interval(6, 9)], Interval(1, 2)))
        self.assertEqual([[1, 2], [3, 5], [6, 9]], s.insert([Interval(3, 5), Interval(6, 9)], Interval(1, 2)))
        self.assertEqual([[1, 5], [6, 9]], s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5)))
        self.assertEqual([[1, 2], [3, 10], [12, 16]], s.insert(
            [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 8)))
        self.assertEqual([[5, 7]], s.insert([], Interval(5, 7)))
        self.assertEqual([[1, 5]], s.insert([Interval(1, 5)], Interval(2, 3)))


if __name__ == '__main__':
    unittest.main()
