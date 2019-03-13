import unittest

from BackTracking.q200_number_of_islands import Solution


class TestNumberOfIslands(unittest.TestCase):
    """Test q200_number_of_islands.py"""

    def test_number_of_islands(self):
        s = Solution()

        self.assertEqual(1, s.numIslands(
            [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]))
        self.assertEqual(3, s.numIslands(
            [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]))


if __name__ == '__main__':
    unittest.main()
