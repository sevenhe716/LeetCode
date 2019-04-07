import unittest

from BitManipulation.q190_reverse_bits import Solution


class TestReverseBits(unittest.TestCase):
    """Test q190_reverse_bits.py"""

    def test_reverse_bits(self):
        s = Solution()

        self.assertEqual(964176192, s.reverseBits(43261596))
        self.assertEqual(3221225471, s.reverseBits(4294967293))


if __name__ == '__main__':
    unittest.main()
