import unittest

from Heap.q857_minimum_cost_to_hire_k_workers import Solution1


class TestMinimumCostToHireKWorkers(unittest.TestCase):
    """Test q857_minimum_cost_to_hire_k_workers.py"""

    def test_minimum_cost_to_hire_k_workers(self):
        s = Solution1()

        self.assertEqual(105.00000, s.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], K=2))
        self.assertEqual(30.66667, s.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3))


if __name__ == '__main__':
    unittest.main()
