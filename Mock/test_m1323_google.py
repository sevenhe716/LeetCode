import unittest

from Mock.m1323_google import Solution


class TestGoogle(unittest.TestCase):
    """Test m1323_google.py"""

    def test_google(self):
        s = Solution()

        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0], s.calcEquation([["a", "b"], ["b", "c"]],
                                                                     [2.0, 3.0],
                                                                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],
                                                                      ["x", "x"]]))

    if __name__ == '__main__':
        unittest.main()
