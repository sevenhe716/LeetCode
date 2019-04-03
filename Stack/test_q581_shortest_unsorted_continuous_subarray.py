import unittest

from Stack.q581_shortest_unsorted_continuous_subarray import Solution


class TestShortestUnsortedContinuousSubarray(unittest.TestCase):
    """Test q581_shortest_unsorted_continuous_subarray.py"""

    def test_shortest_unsorted_continuous_subarray(self):
        s = Solution()

        self.assertEqual(5, s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
        self.assertEqual(0, s.findUnsortedSubarray([2, 3, 4]))
        self.assertEqual(3, s.findUnsortedSubarray([3, 4, 2]))


if __name__ == '__main__':
    unittest.main()
