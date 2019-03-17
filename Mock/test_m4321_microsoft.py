import unittest

from Mock.m4321_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4321_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-2, s.maxSubArray([-2]))


if __name__ == '__main__':
    unittest.main()
