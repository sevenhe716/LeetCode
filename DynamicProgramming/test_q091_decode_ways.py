import unittest

from DynamicProgramming.q091_decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    """Test q091_decode_ways.py"""

    def test_decode_ways(self):
        s = Solution()

        self.assertEqual(0, s.numDecodings(''))
        self.assertEqual(1, s.numDecodings('10'))
        self.assertEqual(1, s.numDecodings('110'))
        self.assertEqual(1, s.numDecodings('2'))
        self.assertEqual(0, s.numDecodings('02'))
        self.assertEqual(0, s.numDecodings('30'))
        self.assertEqual(0, s.numDecodings('200'))
        self.assertEqual(1, s.numDecodings('201'))
        self.assertEqual(2, s.numDecodings('12'))
        self.assertEqual(3, s.numDecodings('226'))
        self.assertEqual(5, s.numDecodings('2226'))
        self.assertEqual(3, s.numDecodings('226789'))
        self.assertEqual(2, s.numDecodings('2026789'))


if __name__ == '__main__':
    unittest.main()
