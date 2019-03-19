import unittest

from Mock.m1333_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1333_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual(1, s.wordsTyping(rows=2, cols=8, sentence=["hello", "world"]))
        self.assertEqual(2, s.wordsTyping(rows=3, cols=6, sentence=["a", "bcd", "e"]))
        self.assertEqual(1, s.wordsTyping(rows=4, cols=5, sentence=["I", "had", "apple", "pie"]))
        self.assertEqual(10, s.wordsTyping(rows=8, cols=7, sentence=["f", "p", "a"]))


if __name__ == '__main__':
    unittest.main()
