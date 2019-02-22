import unittest

from BackTracking.q079_word_search import Solution


class TestWordSearch(unittest.TestCase):
    """Test q079_word_search.py"""

    def test_word_search(self):
        s = Solution()

        self.assertEqual(True, s.exist([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'ABCCED'))

        self.assertEqual(True, s.exist([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'SEE'))

        self.assertEqual(False, s.exist([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'ABCB'))

if __name__ == '__main__':
    unittest.main()
