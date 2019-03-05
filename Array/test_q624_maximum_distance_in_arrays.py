import unittest

from Array.q624_maximum_distance_in_arrays import Solution1


class TestMaximumDistanceInArrays(unittest.TestCase):
    """Test q624_maximum_distance_in_arrays.py"""

    def test_maximum_distance_in_arrays(self):
        s = Solution1()

        self.assertEqual(4, s.maxDistance([[1, 2, 3],
                                           [4, 5],
                                           [1, 2, 3]]))
        self.assertEqual(3, s.maxDistance([[1, 2, 3, 5],
                                           [3, 4],
                                           [2, 3]]))
        self.assertEqual(4, s.maxDistance([[1, 2, 3, 5],
                                           [1, 3, 4],
                                           [2, 3]]))
        self.assertEqual(4, s.maxDistance([[1, 2, 3, 5],
                                           [3, 4, 5],
                                           [2, 3]]))
        self.assertEqual(4, s.maxDistance([[1, 2, 3, 5],
                                           [1, 3, 4, 5],
                                           [2, 3]]))
        self.assertEqual(3, s.maxDistance([[1, 5],
                                           [3, 4]]))


if __name__ == '__main__':
    unittest.main()
