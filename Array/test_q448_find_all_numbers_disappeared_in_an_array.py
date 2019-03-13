import unittest

from Array.q448_find_all_numbers_disappeared_in_an_array import Solution1


class TestFindAllNumbersDisappearedInAnArray(unittest.TestCase):
    """Test q448_find_all_numbers_disappeared_in_an_array.py"""

    def test_find_all_numbers_disappeared_in_an_array(self):
        s = Solution1()

        self.assertEqual([5, 6], s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
