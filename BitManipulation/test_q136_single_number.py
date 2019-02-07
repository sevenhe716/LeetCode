import unittest

from BitManipulation.q136_single_number import Solution


class TestSingleNumber(unittest.TestCase):
    """Test q136_single_number.py"""

    def test_single_number(self):
        s = Solution()

        self.assertEqual(1, s.singleNumber([2, 2, 1]))
        self.assertEqual(4, s.singleNumber([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
