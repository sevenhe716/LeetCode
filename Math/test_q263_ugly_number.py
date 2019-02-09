import unittest

from Math.q263_ugly_number import Solution


class TestUglyNumber(unittest.TestCase):
    """Test q263_ugly_number.py"""

    def test_ugly_number(self):
        s = Solution()

        self.assertEqual(False, s.isUgly(-6))
        self.assertEqual(False, s.isUgly(0))
        self.assertEqual(True, s.isUgly(1))
        self.assertEqual(True, s.isUgly(6))
        self.assertEqual(True, s.isUgly(8))
        self.assertEqual(False, s.isUgly(14))


if __name__ == '__main__':
    unittest.main()
