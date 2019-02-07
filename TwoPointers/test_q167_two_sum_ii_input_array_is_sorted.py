import unittest

from TwoPointers.q167_two_sum_ii_input_array_is_sorted import Solution


class TestTwoSumIiInputArrayIsSorted(unittest.TestCase):
    """Test q167_two_sum_ii_input_array_is_sorted.py"""

    def test_two_sum_ii_input_array_is_sorted(self):
        s = Solution()

        self.assertEqual([1, 2], s.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([2, 3], s.twoSum([5,25,75], 100))


if __name__ == '__main__':
    unittest.main()
