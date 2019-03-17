import unittest

from common import test_by_reflect


class TestAmazon(unittest.TestCase):
    """Test m3212_amazon.py"""

    def test_amazon(self):
        commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        params = [[], [-2], [0], [-3], [], [], [], []]
        res = [None, None, None, None, -3, None, 0, -2]

        test_by_reflect(self, 'm2212_amazon', commands, params, res)


if __name__ == '__main__':
    unittest.main()
