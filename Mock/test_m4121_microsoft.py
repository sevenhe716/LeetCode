import unittest

from Mock.m4121_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4121_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        s.merge(nums1, 3, nums2, 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)


if __name__ == '__main__':
    unittest.main()
