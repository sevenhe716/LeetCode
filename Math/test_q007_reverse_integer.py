import unittest

from Math.q007_reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    """Test q007_reverse_integer.py"""

    def test_reverse_integer(self):
        s = Solution()
        self.assertEqual(321, s.reverse(123))
        self.assertEqual(-321, s.reverse(-123))
        self.assertEqual(21, s.reverse(120))
        self.assertEqual(201, s.reverse(10200))
        self.assertEqual(0, s.reverse(0))
        self.assertEqual(1, s.reverse(1))
        self.assertEqual(-1, s.reverse(-1))
        self.assertEqual(0, s.reverse(-2147483648))
        self.assertEqual(0, s.reverse(2147483647))
        self.assertEqual(0, s.reverse(1147483647))


if __name__ == '__main__':
    unittest.main()
