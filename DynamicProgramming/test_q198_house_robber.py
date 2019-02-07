import unittest

from DynamicProgramming.q198_house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    """Test q198_house_robber.py"""

    def test_house_robber(self):
        s = Solution()

        self.assertEqual(2, s.rob([2]))
        self.assertEqual(2, s.rob([2, 1]))
        self.assertEqual(3, s.rob([1, 3, 1]))
        self.assertEqual(4, s.rob([2, 3, 2]))
        self.assertEqual(4, s.rob([1, 2, 3, 1]))
        self.assertEqual(12, s.rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
