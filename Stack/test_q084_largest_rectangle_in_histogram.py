import unittest

from Stack.q084_largest_rectangle_in_histogram import Solution


class TestLargestRectangleInHistogram(unittest.TestCase):
    """Test q084_largest_rectangle_in_histogram.py"""

    def test_largest_rectangle_in_histogram(self):
        s = Solution()

        self.assertEqual(10, s.largestRectangleArea([2, 1, 5, 6, 2, 3]))


if __name__ == '__main__':
    unittest.main()
