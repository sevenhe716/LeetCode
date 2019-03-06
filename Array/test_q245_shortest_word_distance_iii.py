import unittest

from Array.q245_shortest_word_distance_iii import Solution


class TestShortestWordDistanceIii(unittest.TestCase):
    """Test q245_shortest_word_distance_iii.py"""

    def test_shortest_word_distance_iii(self):
        s = Solution()

        self.assertEqual(1, s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
        self.assertEqual(3, s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))


if __name__ == '__main__':
    unittest.main()
