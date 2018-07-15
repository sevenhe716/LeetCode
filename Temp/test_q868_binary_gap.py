import unittest

from Temp.q868_binary_gap import Solution


class TestBinaryGap(unittest.TestCase):
    """Test q868_binary_gap.py"""

    def test_binary_gap(self):
        s = Solution()

        self.assertEqual(2, s.binaryGap(5))
        self.assertEqual(2, s.binaryGap(22))
        self.assertEqual(1, s.binaryGap(6))
        self.assertEqual(0, s.binaryGap(8))
        self.assertEqual(0, s.binaryGap(0))
        self.assertEqual(1, s.binaryGap(7))
        self.assertEqual(0, s.binaryGap(1))
        self.assertEqual(2, s.binaryGap(21))

if __name__ == '__main__':
    unittest.main()
