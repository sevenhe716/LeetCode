import unittest

from DynamicProgramming.q847_shortest_path_visiting_all_nodes import Solution


class TestShortestPathVisitingAllNodes(unittest.TestCase):
    """Test q847_shortest_path_visiting_all_nodes.py"""

    def test_shortest_path_visiting_all_nodes(self):
        s = Solution()

        self.assertEqual(4, s.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
        self.assertEqual(4, s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
        self.assertEqual(6, s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2, 5], [4]]))


if __name__ == '__main__':
    unittest.main()
