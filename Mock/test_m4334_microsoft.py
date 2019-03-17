import unittest

from Mock.m4334_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4334_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(2, s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
        self.assertEqual(2.5, s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))


if __name__ == '__main__':
    unittest.main()
