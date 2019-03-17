# Time:  O(n)
# Space: O(1)

# Ideas:
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy1, dummy2 = ListNode(0), ListNode(1)
        dummy1.next, dummy2.next = l1, l2
        carry, cur1, cur2 = 0, dummy1, dummy2

        while cur1.next and cur2.next:
            carry, cur1.next.val = divmod(cur1.next.val + cur2.next.val + carry, 10)
            cur1, cur2 = cur1.next, cur2.next

        if not cur1.next:
            cur1.next = cur2.next

        while cur1.next and carry == 1:
            carry, cur1.next.val = divmod(cur1.next.val + carry, 10)
            cur1 = cur1.next

        if carry == 1:
            cur1.next = ListNode(1)

        return dummy1.next

