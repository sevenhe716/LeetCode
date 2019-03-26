import unittest

from Graph.q399_evaluate_division import Solution


class TestEvaluateDivision(unittest.TestCase):
    """Test q399_evaluate_division.py"""

    def test_evaluate_division(self):
        s = Solution()

        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0], s.calcEquation([["a", "b"], ["b", "c"]],
                                                                     [2.0, 3.0],
                                                                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],
                                                                      ["x", "x"]]))

if __name__ == '__main__':
    unittest.main()
