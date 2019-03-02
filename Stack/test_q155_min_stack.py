import unittest

from common import test_by_reflect


class TestMinStack(unittest.TestCase):
    """Test q155_min_stack.py"""

    def test_min_stack(self):
        commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        params = [[], [-2], [0], [-3], [], [], [], []]
        res = [None, None, None, None, -3, None, 0, -2]
        test_by_reflect(self, 'q155_min_stack', commands, params, res)


if __name__ == '__main__':
    unittest.main()
