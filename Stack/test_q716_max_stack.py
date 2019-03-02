import unittest

from common import test_by_reflect


class TestMaxStack(unittest.TestCase):
    """Test q716_max_stack.py"""

    def test_max_stack(self):
        commands = ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
        params = [[], [5], [1], [5], [], [], [], [], [], []]
        res = [None, None, None, None, 5, 5, 1, 5, 1, 5]
        test_by_reflect(self, 'q716_max_stack', commands, params, res)

        commands = ["MaxStack", "push", "peekMax", "popMax"]
        params = [[], [5], [], []]
        res = [None, None, 5, 5]
        test_by_reflect(self, 'q716_max_stack', commands, params, res)

        commands = ["MaxStack", "push", "popMax", "push", "push", "popMax", "pop", "push", "push", "peekMax", "popMax",
                    "push", "pop", "push", "push"]
        params = [[], [74], [], [89], [67], [], [], [61], [-77], [], [], [81], [], [-71], [32]]
        res = [None, None, 74, None, None, 89, 67, None, None, 61, 61, None, 81, None, None]
        test_by_reflect(self, 'q716_max_stack', commands, params, res)


if __name__ == '__main__':
    unittest.main()
