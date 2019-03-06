import unittest

from common import test_by_reflect


class TestShortestWordDistanceIi(unittest.TestCase):
    """Test q244_shortest_word_distance_ii.py"""

    def test_shortest_word_distance_ii(self):
        commands = ["WordDistance", "shortest", "shortest"]
        params = [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
        res = [None, 3, 1]

        test_by_reflect(self, 'q244_shortest_word_distance_ii', commands, params, res)


if __name__ == '__main__':
    unittest.main()
