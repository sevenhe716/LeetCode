import unittest

from Array.q243_shortest_word_distance import Solution


class TestShortestWordDistance(unittest.TestCase):
    """Test q243_shortest_word_distance.py"""

    def test_shortest_word_distance(self):
        s = Solution()

        self.assertEqual(3, s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
        self.assertEqual(1, s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))
        self.assertEqual(1, s.shortestDistance(["a", "c", "a", "b"], "a", "b"))


if __name__ == '__main__':
    unittest.main()
