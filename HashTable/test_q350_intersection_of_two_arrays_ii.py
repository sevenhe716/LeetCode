import unittest

from HashTable.q350_intersection_of_two_arrays_ii import Solution


class TestIntersectionOfTwoArraysIi(unittest.TestCase):
    """Test q350_intersection_of_two_arrays_ii.py"""

    def test_intersection_of_two_arrays_ii(self):
        s = Solution()

        self.assertEqual(sorted([2, 2]), sorted(s.intersect([1, 2, 2, 1], [2, 2])))
        self.assertEqual(sorted([4, 9]), sorted(s.intersect([4, 9, 5], [9, 4, 9, 8, 4])))


if __name__ == '__main__':
    unittest.main()
