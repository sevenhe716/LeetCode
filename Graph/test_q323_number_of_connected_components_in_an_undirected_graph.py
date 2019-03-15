import unittest

from Graph.q323_number_of_connected_components_in_an_undirected_graph import Solution1


class TestNumberOfConnectedComponentsInAnUndirectedGraph(unittest.TestCase):
    """Test q323_number_of_connected_components_in_an_undirected_graph.py"""

    def test_number_of_connected_components_in_an_undirected_graph(self):
        s = Solution1()

        self.assertEqual(2, s.countComponents(5, [[0, 1], [2, 1], [3, 4]]))
        # self.assertEqual(1, s.countComponents(5, [[0, 1], [2, 1], [3, 2], [3, 4]]))


if __name__ == '__main__':
    unittest.main()
