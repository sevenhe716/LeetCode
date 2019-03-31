import unittest

from UnionFind.q305_number_of_islands_ii import Solution1


class TestNumberOfIslandsIi(unittest.TestCase):
    """Test q305_number_of_islands_ii.py"""

    def test_number_of_islands_ii(self):
        s = Solution1()

        self.assertEqual([1, 1, 2, 3], s.numIslands21(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))


if __name__ == '__main__':
    unittest.main()
