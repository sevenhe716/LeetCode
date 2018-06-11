import unittest

from Array.q849_maximize_distance_to_closest_person import Solution1


class TestMaximizeDistanceToClosestPerson(unittest.TestCase):
    """Test q849_maximize_distance_to_closest_person.py"""

    def test_maximize_distance_to_closest_person(self):
        s = Solution1()

        self.assertEqual(2, s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
        self.assertEqual(3, s.maxDistToClosest([1, 0, 0, 0]))
        self.assertEqual(4, s.maxDistToClosest([0, 0, 0, 0, 1]))
        self.assertEqual(4, s.maxDistToClosest([0, 0, 0, 0, 1, 0, 0, 1, 1]))
        self.assertEqual(2, s.maxDistToClosest([0, 1, 1, 1, 0, 0, 1, 0, 0]))
        self.assertEqual(2, s.maxDistToClosest([0, 0, 1, 1, 1, 0, 0, 1]))
        self.assertEqual(3, s.maxDistToClosest([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
