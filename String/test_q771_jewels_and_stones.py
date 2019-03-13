import unittest

from String.q771_jewels_and_stones import Solution


class TestJewelsAndStones(unittest.TestCase):
    """Test q771_jewels_and_stones.py"""

    def test_jewels_and_stones(self):
        s = Solution()

        self.assertEqual(3, s.numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(0, s.numJewelsInStones("z", "ZZ"))
        self.assertEqual(3, s.numJewelsInStones("ebd", "bbb"))


if __name__ == '__main__':
    unittest.main()
