import unittest

from Mock.m4221_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4221_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(6, s.lowestCommonAncestor(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=8))
        self.assertEqual(2, s.lowestCommonAncestor(root=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p=2, q=4))


if __name__ == '__main__':
    unittest.main()
