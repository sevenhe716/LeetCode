import unittest

from common import test_by_reflect


class TestImplementStackUsingQueues(unittest.TestCase):
    """Test q225_implement_stack_using_queues.py"""

    def test_implement_stack_using_queues(self):
        commands = ["MyStack", "push", "push", "top", "pop", "empty"]
        params = [[], [1], [2], [], [], []]
        res = [None, None, None, 2, 2, False]
        test_by_reflect(self, 'q225_implement_stack_using_queues', commands, params, res)


if __name__ == '__main__':
    unittest.main()
