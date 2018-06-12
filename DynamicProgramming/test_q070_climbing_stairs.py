import unittest

from DynamicProgramming.q070_climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    """Test q070_climbing_stairs.py"""

    def test_climbing_stairs(self):
        s = Solution()

        self.assertEqual(1, s.climbStairs(1))
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))


if __name__ == '__main__':
    unittest.main()
