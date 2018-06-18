import unittest

from BFS.q854_ksimilar_strings import Solution1


class TestKsimilarStrings(unittest.TestCase):
    """Test q854_ksimilar_strings.py"""

    def test_ksimilar_strings(self):
        s = Solution1()

        # self.assertEqual(1, s.kSimilarity('ab', 'ba'))
        # self.assertEqual(2, s.kSimilarity('abc', 'bca'))
        # self.assertEqual(2, s.kSimilarity('abac', 'baca'))
        # self.assertEqual(2, s.kSimilarity('aabc', 'abca'))
        # self.assertEqual(3, s.kSimilarity('bccaba', 'abacbc'))
        self.assertEqual(5, s.kSimilarity('aabbccddee', 'dcacbedbae'))
        self.assertEqual(6, s.kSimilarity('aabbccddee', 'cdacbeebad'))
        self.assertEqual(6, s.kSimilarity("aabbccddee", "ceacdbaebd"))


if __name__ == '__main__':
    unittest.main()
