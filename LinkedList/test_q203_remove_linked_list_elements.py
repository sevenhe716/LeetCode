import unittest

from LinkedList.q203_remove_linked_list_elements import Solution
from common import ListNode


class TestRemoveLinkedListElements(unittest.TestCase):
    """Test q203_remove_linked_list_elements.py"""

    def test_remove_linked_list_elements(self):
        s = Solution()

        self.assertEqual(None,
                         s.removeElements(ListNode.generate([]), 6))
        self.assertEqual(None,
                         s.removeElements(ListNode.generate([6, 6]), 6))
        self.assertEqual(None,
                         s.removeElements(ListNode.generate([6]), 6))
        self.assertEqual(ListNode.generate([1, 2, 3, 4, 5]), s.removeElements(ListNode.generate([1, 2, 6, 3, 4, 5, 6]), 6))


if __name__ == '__main__':
    unittest.main()
