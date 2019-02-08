import unittest

from BitManipulation.q231_power_of_two import Solution


class TestPowerOfTwo(unittest.TestCase):
    """Test q231_power_of_two.py"""

    def test_power_of_two(self):
        s = Solution()

        self.assertEqual(False, s.isPowerOfTwo(0))
        self.assertEqual(True, s.isPowerOfTwo(1))
        self.assertEqual(True, s.isPowerOfTwo(16))
        self.assertEqual(False, s.isPowerOfTwo(218))


if __name__ == '__main__':
    unittest.main()
