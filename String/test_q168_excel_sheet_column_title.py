import unittest

from String.q168_excel_sheet_column_title import Solution


class TestExcelSheetColumnTitle(unittest.TestCase):
    """Test q168_excel_sheet_column_title.py"""

    def test_excel_sheet_column_title(self):
        s = Solution()

        self.assertEqual('A', s.convertToTitle(1))
        self.assertEqual('Z', s.convertToTitle(26))
        self.assertEqual('AB', s.convertToTitle(28))
        self.assertEqual('ZY', s.convertToTitle(701))


if __name__ == '__main__':
    unittest.main()
