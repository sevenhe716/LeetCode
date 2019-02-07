import unittest

from String.q171_excel_sheet_column_number import Solution


class TestExcelSheetColumnNumber(unittest.TestCase):
    """Test q171_excel_sheet_column_number.py"""

    def test_excel_sheet_column_number(self):
        s = Solution()

        self.assertEqual(1, s.titleToNumber('A'))
        self.assertEqual(28, s.titleToNumber('AB'))
        self.assertEqual(701, s.titleToNumber('ZY'))


if __name__ == '__main__':
    unittest.main()
