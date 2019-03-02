import unittest

from HashTable.q760_find_anagram_mappings import Solution


class TestFindAnagramMappings(unittest.TestCase):
    """Test q760_find_anagram_mappings.py"""

    def test_find_anagram_mappings(self):
        s = Solution()

        self.assertEqual([1, 4, 3, 2, 0], s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
        # self.assertEqual([2, 4, 3, 1, 0], s.anagramMappings([32, 28, 46, 32, 50], [50, 32, 32, 46, 28]))


if __name__ == '__main__':
    unittest.main()
