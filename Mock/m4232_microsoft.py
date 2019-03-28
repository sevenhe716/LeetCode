# Time:  O(n)
# Space: O(1)

# Ideas:
# mark


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            # pre = cur.next
            # post = cur.next.next
            # cur.next, post.next, pre.next = post, pre, post.next
            cur.next.next.next, cur.next.next, cur.next = cur.next, cur.next.next.next, cur.next.next
            cur = cur.next.next
            # cur.next, cur.next.next.next, cur.next.next = cur.next.next, cur.next, cur.next.next.next
            # cur = cur.next.next
        return dummy.next