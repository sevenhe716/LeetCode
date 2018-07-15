import unittest

from Temp.q869_reordered_power_of_2 import Solution


class TestReorderedPowerOf2(unittest.TestCase):
    """Test q869_reordered_power_of_2.py"""

    def test_reordered_power_of_2(self):
        s = Solution()

        self.assertEqual(True, s.reorderedPowerOf2(1))
        self.assertEqual(False, s.reorderedPowerOf2(10))
        self.assertEqual(True, s.reorderedPowerOf2(16))
        self.assertEqual(False, s.reorderedPowerOf2(24))
        self.assertEqual(True, s.reorderedPowerOf2(46))


if __name__ == '__main__':
    unittest.main()
