import unittest

from BinarySearch.q163_missing_ranges import Solution


class TestMissingRanges(unittest.TestCase):
    """Test q163_missing_ranges.py"""

    def test_missing_ranges(self):
        s = Solution()

        self.assertEqual(["0->99"], s.findMissingRanges([], 0, 99))
        self.assertEqual(["1"], s.findMissingRanges([], 1, 1))
        self.assertEqual(["2", "4->49", "51->74", "76->99"], s.findMissingRanges([0, 1, 3, 50, 75], 0, 99))


if __name__ == '__main__':
    unittest.main()
