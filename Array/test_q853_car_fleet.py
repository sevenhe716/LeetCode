import unittest

from Array.q853_car_fleet import Solution


class TestCarFleet(unittest.TestCase):
    """Test q853_car_fleet.py"""

    def test_car_fleet(self):
        s = Solution()

        self.assertEqual(3, s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
        self.assertEqual(0, s.carFleet(12, [], []))
        self.assertEqual(1, s.carFleet(10, [0, 4, 2], [2, 1, 3]))
        self.assertEqual(2, s.carFleet(10, [0, 4, 2], [0.01, 1, 3]))
        self.assertEqual(1, s.carFleet(10, [0], [2]))


if __name__ == '__main__':
    unittest.main()
