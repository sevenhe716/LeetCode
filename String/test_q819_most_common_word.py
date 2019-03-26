import unittest

from String.q819_most_common_word import Solution


class TestMostCommonWord(unittest.TestCase):
    """Test q819_most_common_word.py"""

    def test_most_common_word(self):
        s = Solution()

        self.assertEqual('ball', s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                                                  banned=["hit"]))
        self.assertEqual('b', s.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c",
                                               banned=["a"]))


if __name__ == '__main__':
    unittest.main()
