import unittest

from BitManipulation.q137_single_number_ii import Solution


class TestSingleNumberIi(unittest.TestCase):
    """Test q137_single_number_ii.py"""

    def test_single_number_ii(self):
        s = Solution()

        self.assertEqual(3, s.singleNumber([2, 2, 3, 2]))
        self.assertEqual(99, s.singleNumber([0, 1, 0, 1, 0, 1, 99]))


if __name__ == '__main__':
    unittest.main()
