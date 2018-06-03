import unittest

from TwoPointers.q042_trapping_rain_water import Solution


class TestTrappingRainWater(unittest.TestCase):
    """Test q042_trapping_rain_water.py"""

    def test_trapping_rain_water(self):
        s = Solution()

        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


if __name__ == '__main__':
    unittest.main()
