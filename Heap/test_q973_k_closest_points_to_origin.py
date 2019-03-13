import unittest

from Heap.q973_k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    """Test q973_k_closest_points_to_origin.py"""

    def test_k_closest_points_to_origin(self):
        s = Solution()

        self.assertEqual([[-2, 2]], s.kClosest([[1, 3], [-2, 2]], 1))
        self.assertEqual([[3, 3], [-2, 4]], s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


if __name__ == '__main__':
    unittest.main()
