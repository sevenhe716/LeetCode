import unittest

from Math.q326_power_of_three import Solution


class TestPowerOfThree(unittest.TestCase):
    """Test q326_power_of_three.py"""

    def test_power_of_three(self):
        s = Solution()

        self.assertEqual(True, s.isPowerOfThree(27))
        self.assertEqual(False, s.isPowerOfThree(0))
        self.assertEqual(True, s.isPowerOfThree(9))
        self.assertEqual(False, s.isPowerOfThree(45))


if __name__ == '__main__':
    unittest.main()
