import unittest

from Temp.q876_middle_of_the_linked_list import Solution
import common

class TestMiddleOfTheLinkedList(unittest.TestCase):
    """Test q876_middle_of_the_linked_list.py"""

    def test_middle_of_the_linked_list(self):
        s = Solution()

        self.assertEqual(, s.middleNode(common.ListNode.generate([1,2,3,4,5])))
        self.assertEqual(, s.middleNode(common.ListNode.generate([1,2,3,4,5,6])))


if __name__ == '__main__':
    unittest.main()
