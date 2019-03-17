import unittest

from Mock.m4332_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4332_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], s.spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))

        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], s.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]))

        self.assertEqual([6, 9, 7], s.spiralOrder([[6, 9, 7]]))

if __name__ == '__main__':
    unittest.main()
