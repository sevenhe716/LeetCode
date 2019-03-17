import unittest

from Mock.m4233_microsoft import Solution


class TestMicrosoft(unittest.TestCase):
    """Test m4233_microsoft.py"""

    def test_microsoft(self):
        s = Solution()

        self.assertEqual(sorted(["eat", "oath"]), sorted(s.findWords(words=["oath", "pea", "eat", "rain"], board=[
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ])))

if __name__ == '__main__':
    unittest.main()
