import unittest

from q711_number_of_distinct_islands_ii import Solution


class TestNumberOfDistinctIslandsIi(unittest.TestCase):
    """Test q711_number_of_distinct_islands_ii.py"""

    def test_number_of_distinct_islands_ii(self):
        s = Solution()

        self.assertEqual(1, s.numDistinctIslands2([[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]))
        self.assertEqual(2, s.numDistinctIslands2([[1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]))


if __name__ == '__main__':
    unittest.main()
