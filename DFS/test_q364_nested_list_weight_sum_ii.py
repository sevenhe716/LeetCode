import unittest

from DFS.q364_nested_list_weight_sum_ii import Solution


class TestNestedListWeightSumIi(unittest.TestCase):
    """Test q364_nested_list_weight_sum_ii.py"""

    def test_nested_list_weight_sum_ii(self):
        s = Solution()

        self.assertEqual(8, s.depthSumInverse([[1, 1], 2, [1, 1]]))
        self.assertEqual(17, s.depthSumInverse([1, [4, [6]]]))


if __name__ == '__main__':
    unittest.main()
