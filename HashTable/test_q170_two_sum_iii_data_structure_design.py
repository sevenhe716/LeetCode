import unittest

from common import test_by_reflect


class TestTwoSumIiiDataStructureDesign(unittest.TestCase):
    """Test q170_two_sum_iii_data_structure_design.py"""

    def test_two_sum_iii_data_structure_design(self):
        commands = ["TwoSum1", "add", "add", "add", "find", "find"]
        params = [[], [1], [3], [5], [4], [7]]
        res = [None, None, None, None, True, False]
        test_by_reflect(self, 'q170_two_sum_iii_data_structure_design', commands, params, res)

        commands = ["TwoSum1", "add", "find"]
        params = [[], [0], [0]]
        res = [None, None, False]
        test_by_reflect(self, 'q170_two_sum_iii_data_structure_design', commands, params, res)

if __name__ == '__main__':
    unittest.main()
