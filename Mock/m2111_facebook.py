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
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1:
            return l2
        if not l2:
            return l1

        cur = dummy = ListNode(0)

        if l1.val <= l2.val:
            cur.next = l1
            other = l2
        else:
            cur.next = l2
            other = l1

        while cur.next and other:
            while cur.next and cur.next.val <= other.val:
                cur = cur.next
            if cur.next:
                cur.next, other, cur = other, cur.next, other
        if other:
            cur.next = other
        return dummy.next