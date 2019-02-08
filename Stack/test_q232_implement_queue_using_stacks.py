import unittest

from Stack.q232_implement_queue_using_stacks import MyQueue


class TestImplementQueueUsingStacks(unittest.TestCase):
    """Test q232_implement_queue_using_stacks.py"""

    def test_implement_queue_using_stacks(self):
        queue = MyQueue()

        queue.push(1)
        queue.push(2)
        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        self.assertEqual(False, queue.empty())


if __name__ == '__main__':
    unittest.main()
