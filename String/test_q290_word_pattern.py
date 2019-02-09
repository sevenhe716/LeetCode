import unittest

from String.q290_word_pattern import Solution1


class TestWordPattern(unittest.TestCase):
    """Test q290_word_pattern.py"""

    def test_word_pattern(self):
        s = Solution1()

        self.assertEqual(True, s.wordPattern("abba", "dog cat cat dog"))
        self.assertEqual(False, s.wordPattern("abba", "dog cat cat fish"))
        self.assertEqual(False, s.wordPattern("aaaa", "dog cat cat dog"))
        self.assertEqual(False, s.wordPattern("abba", "dog dog dog dog"))


if __name__ == '__main__':
    unittest.main()
