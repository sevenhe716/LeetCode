import unittest

from DynamicProgramming.q746_min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    """Test q746_min_cost_climbing_stairs.py"""

    def test_min_cost_climbing_stairs(self):
        s = Solution()

        self.assertEqual(15, s.minCostClimbingStairs([10, 15, 20]))
        self.assertEqual(10, s.minCostClimbingStairs([10, 15]))
        self.assertEqual(6, s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


if __name__ == '__main__':
    unittest.main()
