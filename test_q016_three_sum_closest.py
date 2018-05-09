import unittest

from q016_three_sum_closest import Solution


class TestThreeSumClosest(unittest.TestCase):
    """Test q016_three_sum_closest.py"""

    def test_three_sum_closest(self):
        s = Solution()

        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 2))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(0, s.threeSumClosest([0, 2, 1, -3], 1))


if __name__ == '__main__':
    unittest.main()
