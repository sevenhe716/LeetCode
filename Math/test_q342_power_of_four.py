import unittest

from Math.q342_power_of_four import Solution2


class TestPowerOfFour(unittest.TestCase):
    """Test q342_power_of_four.py"""

    def test_power_of_four(self):
        s = Solution2()

        self.assertEqual(True, s.isPowerOfFour(1))
        self.assertEqual(True, s.isPowerOfFour(16))
        self.assertEqual(False, s.isPowerOfFour(5))


if __name__ == '__main__':
    unittest.main()
