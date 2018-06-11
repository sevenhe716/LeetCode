import unittest

from Math.q050_pow import Solution


class TestPow(unittest.TestCase):
    """Test q050_pow.py"""

    def test_pow(self):
        s = Solution()

        self.assertAlmostEqual(1024.00000, s.myPow(2.00000, 10))
        self.assertAlmostEqual(9.26100, s.myPow(2.10000, 3))
        self.assertAlmostEqual(0.25000, s.myPow(2.00000, -2))
        self.assertAlmostEqual(1024.00000, s.myPow(-2.00000, 10))
        self.assertAlmostEqual(-9.26100, s.myPow(-2.10000, 3))
        self.assertAlmostEqual(0.25000, s.myPow(-2.00000, -2))
        self.assertAlmostEqual(-0.125000, s.myPow(-2.00000, -3))
        self.assertAlmostEqual(0, s.myPow(0, -2))
        self.assertAlmostEqual(0, s.myPow(0, 2))
        self.assertAlmostEqual(1, s.myPow(3.2, 0))
        self.assertAlmostEqual(1, s.myPow(-3.2, 0))


if __name__ == '__main__':
    unittest.main()
