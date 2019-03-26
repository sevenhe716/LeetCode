import unittest

from Trie.q212_word_search_ii import Solution


class TestWordSearchIi(unittest.TestCase):
    """Test q212_word_search_ii.py"""

    def test_word_search_ii(self):
        s = Solution()

        self.assertEqual(sorted(["eat", "oath"]), sorted(s.findWords(words=["oath", "pea", "eat", "rain"], board=[
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ])))


if __name__ == '__main__':
    unittest.main()
