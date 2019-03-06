import unittest

from Array.q280_wiggle_sort import Solution


class TestWiggleSort(unittest.TestCase):
    """Test q280_wiggle_sort.py"""

    def test_wiggle_sort(self):
        s = Solution()

        nums = [3, 5, 2, 1, 6, 4]
        s.wiggleSort(nums)
        self.assertEqual([3, 5, 1, 6, 2, 4], nums)


if __name__ == '__main__':
    unittest.main()
