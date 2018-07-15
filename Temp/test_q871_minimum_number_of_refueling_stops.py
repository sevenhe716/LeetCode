import unittest

from Temp.q871_minimum_number_of_refueling_stops import Solution


class TestMinimumNumberOfRefuelingStops(unittest.TestCase):
    """Test q871_minimum_number_of_refueling_stops.py"""

    def test_minimum_number_of_refueling_stops(self):
        s = Solution()

        self.assertEqual(-1, s.minRefuelStops(100, 1, []))
        self.assertEqual(0, s.minRefuelStops(1, 1, []))
        self.assertEqual(-1, s.minRefuelStops(100, 1, [[10, 100]]))
        self.assertEqual(2, s.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))


if __name__ == '__main__':
    unittest.main()
