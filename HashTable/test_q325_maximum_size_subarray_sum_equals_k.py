import unittest

from HashTable.q325_maximum_size_subarray_sum_equals_k import Solution


class TestMaximumSizeSubarraySumEqualsK(unittest.TestCase):
    """Test q325_maximum_size_subarray_sum_equals_k.py"""

    def test_maximum_size_subarray_sum_equals_k(self):
        s = Solution()

        self.assertEqual(ListNode.generate([1, 1, 2, 3, 4, 4]),
                         s.mergeTwoLists(ListNode.generate([1, 2, 4]), ListNode.generate([1, 3, 4])))


if __name__ == '__main__':
    unittest.main()
