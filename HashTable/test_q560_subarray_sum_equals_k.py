import unittest

from HashTable.q560_subarray_sum_equals_k import Solution


class TestSubarraySumEqualsK(unittest.TestCase):
    """Test q560_subarray_sum_equals_k.py"""

    def test_subarray_sum_equals_k(self):
        s = Solution()

        self.assertEqual(2, s.subarraySum([1, 1, 1], 2))


if __name__ == '__main__':
    unittest.main()
