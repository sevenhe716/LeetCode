import unittest

from common import test_by_reflect


class TestImplementQueueUsingStacks(unittest.TestCase):
    """Test q232_implement_queue_using_stacks.py"""

    def test_implement_queue_using_stacks(self):
        commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        params = [[], [1], [2], [], [], []]
        res = [None, None, None, 1, 1, False]
        test_by_reflect(self, 'q232_implement_queue_using_stacks', commands, params, res)


if __name__ == '__main__':
    unittest.main()
