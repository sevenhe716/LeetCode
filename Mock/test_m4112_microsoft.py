import unittest

from Mock.m4112_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4112_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual([3], s.majorityElement([3, 2, 3]))
        self.assertEqual([1, 2], s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
