import unittest

from Array.q189_rotate_array import Solution


class TestRotateArray(unittest.TestCase):
    """Test q189_rotate_array.py"""

    def test_rotate_array(self):
        s = Solution()

        nums = [1, 2, 3, 4, 5, 6, 7]
        s.rotate(nums, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums)

        nums = [-1, -100, 3, 99]
        s.rotate(nums, 2)
        self.assertEqual([3, 99, -1, -100], nums)


if __name__ == '__main__':
    unittest.main()
