import unittest

from Array.q303_range_sum_query_immutable import NumArray


class TestRangeSumQueryImmutable(unittest.TestCase):
    """Test q303_range_sum_query_immutable.py"""

    def test_range_sum_query_immutable(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])

        self.assertEqual(1, num_array.sumRange(0, 2))
        self.assertEqual(-1, num_array.sumRange(2, 5))
        self.assertEqual(-3, num_array.sumRange(0, 5))


if __name__ == '__main__':
    unittest.main()
