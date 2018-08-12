import unittest

from Temp.q878_nth_magical_number import Solution


class TestNthMagicalNumber(unittest.TestCase):
    """Test q878_nth_magical_number.py"""

    def test_nth_magical_number(self):
        s = Solution()

        self.assertEqual(2, s.nthMagicalNumber(1, 2, 3))
        self.assertEqual(6, s.nthMagicalNumber(4, 2, 3))
        self.assertEqual(10, s.nthMagicalNumber(5, 2, 4))
        self.assertEqual(8, s.nthMagicalNumber(3, 6, 4))
        self.assertEqual(8, s.nthMagicalNumber(1000000000, 39999, 40000))


if __name__ == '__main__':
    unittest.main()
