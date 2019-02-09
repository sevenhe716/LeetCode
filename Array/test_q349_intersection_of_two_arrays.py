import unittest

from Array.q349_intersection_of_two_arrays import Solution


class TestIntersectionOfTwoArrays(unittest.TestCase):
    """Test q349_intersection_of_two_arrays.py"""

    def test_intersection_of_two_arrays(self):
        s = Solution()

        self.assertEqual([2], s.intersection([1, 2, 2, 1], [2, 2]))
        self.assertEqual([9, 4], s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))


if __name__ == '__main__':
    unittest.main()
