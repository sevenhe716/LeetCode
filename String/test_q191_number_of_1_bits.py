import unittest

from String.q191_number_of_1_bits import Solution


class TestNumberOf1Bits(unittest.TestCase):
    """Test q191_number_of_1_bits.py"""

    def test_number_of_1_bits(self):
        s = Solution()
        self.assertEqual(3, s.hammingWeight(11))
        self.assertEqual(1, s.hammingWeight(128))
        self.assertEqual(31, s.hammingWeight(4294967293))


if __name__ == '__main__':
    unittest.main()
