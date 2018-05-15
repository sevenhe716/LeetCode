import unittest

from String.q006_zigzag_conversion import SolutionF


class TestZigZagConversion(unittest.TestCase):
    """Test q006_zigzag_conversion.py"""

    def test_ZigZagConversion(self):
        s = SolutionF()
        self.assertEqual("PAHNAPLSIIGYIR", s.convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", s.convert("PAYPALISHIRING", 4))
        self.assertEqual("PAHNAPLSIIYIR", s.convert("PAYPALISHIRIN", 3))
        self.assertEqual("P", s.convert("P", 4))
        self.assertEqual("", s.convert("", 4))
        self.assertEqual("PALYAP", s.convert("PAYPAL", 4))
        self.assertEqual("PYAAPL", s.convert("PAYPAL", 2))
        self.assertEqual("PAY", s.convert("PAY", 1))


if __name__ == '__main__':
    unittest.main()
