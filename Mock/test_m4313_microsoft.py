import unittest

from Mock.m4313_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4313_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(True, s.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5))

        self.assertEqual(False, s.searchMatrix([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20))


if __name__ == '__main__':
    unittest.main()
