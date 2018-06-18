import unittest

from Array.q852_peak_index_in_a_mountain_array import Solution


class TestPeakIndexInAMountainArray(unittest.TestCase):
    """Test q852_peak_index_in_a_mountain_array.py"""

    def test_peak_index_in_a_mountain_array(self):
        s = Solution()

        self.assertEqual(1, s.peakIndexInMountainArray([0, 1, 0]))
        self.assertEqual(1, s.peakIndexInMountainArray([0, 2, 1, 0]))


if __name__ == '__main__':
    unittest.main()
