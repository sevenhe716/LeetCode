import unittest

from PriorityQueue.q857_minimum_cost_to_hire_k_workers import Solution


class TestMinimumCostToHireKWorkers(unittest.TestCase):
    """Test q857_minimum_cost_to_hire_k_workers.py"""

    def test_minimum_cost_to_hire_k_workers(self):
        s = Solution()

        self.assertEqual(105.00000, s.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
        self.assertEqual(30.66667, s.mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))


if __name__ == '__main__':
    unittest.main()
