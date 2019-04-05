import unittest

from BitManipulation.q318_maximum_product_of_word_lengths import Solution


class TestMaximumProductOfWordLengths(unittest.TestCase):
    """Test q318_maximum_product_of_word_lengths.py"""

    def test_maximum_product_of_word_lengths(self):
        s = Solution()

        self.assertEqual(16, s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
        self.assertEqual(4, s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
        self.assertEqual(0, s.maxProduct(["a", "aa", "aaa", "aaaa"]))


if __name__ == '__main__':
    unittest.main()
