import unittest

from q694_number_of_distinct_islands import Solution


class TestNumberOfDistinctIslands(unittest.TestCase):
    """Test q694_number_of_distinct_islands.py"""

    def test_number_of_distinct_islands(self):
        s = Solution()

        self.assertEqual(1, s.numDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
        self.assertEqual(3, s.numDistinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))


if __name__ == '__main__':
    unittest.main()
