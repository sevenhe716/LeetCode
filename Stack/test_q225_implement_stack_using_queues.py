import unittest

from Stack.q225_implement_stack_using_queues import MyStack


class TestImplementStackUsingQueues(unittest.TestCase):
    """Test q225_implement_stack_using_queues.py"""

    def test_implement_stack_using_queues(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.pop())
        self.assertEqual(False, stack.empty())


if __name__ == '__main__':
    unittest.main()
