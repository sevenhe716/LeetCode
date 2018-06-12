import unittest

from DynamicProgramming.q064_minimum_path_sum import Solution


class TestMinimumPathSum(unittest.TestCase):
    """Test q064_minimum_path_sum.py"""

    def test_minimum_path_sum(self):
        s = Solution()

        self.assertEqual(7, s.minPathSum([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))

        self.assertEqual(1, s.minPathSum([
            [1]
        ]))


if __name__ == '__main__':
    unittest.main()
