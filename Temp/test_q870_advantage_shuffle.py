import unittest

from Temp.q870_advantage_shuffle import Solution


class TestAdvantageShuffle(unittest.TestCase):
    """Test q870_advantage_shuffle.py"""

    def test_advantage_shuffle(self):
        s = Solution()

        self.assertEqual([2, 11, 7, 15], s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
        self.assertEqual([24, 32, 8, 12], s.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))


if __name__ == '__main__':
    unittest.main()
