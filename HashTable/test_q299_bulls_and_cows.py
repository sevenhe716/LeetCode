import unittest

from HashTable.q299_bulls_and_cows import Solution1


class TestBullsAndCows(unittest.TestCase):
    """Test q299_bulls_and_cows.py"""

    def test_bulls_and_cows(self):
        s = Solution1()

        self.assertEqual("1A3B", s.getHint5(secret="1807", guess="7810"))
        self.assertEqual("1A1B", s.getHint5(secret="1123", guess="0111"))
        self.assertEqual("3A0B", s.getHint5(secret="1122", guess="1222"))


if __name__ == '__main__':
    unittest.main()
