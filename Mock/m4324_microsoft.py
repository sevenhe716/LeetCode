# Time:  O(n)
# Space: O(1)

# Ideas:
# because last part if less than k, not reverse, so get the length first


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def reverseKGroup(self, head: 'ListNode', k: int) -> 'ListNode':
        dummy = ListNode(0)
        cur = dummy.next = head

        count = 0
        while cur:
            cur = cur.next
            count += 1

        cur = dummy
        for i in range(count // k):
            # head, tail = reverseK()
            tail = cur.next
            pre = cur.next
            post = cur.next.next
            pre.next = None
            # get head and tail
            for j in range(k-1):
                post.next, pre, post = pre, post, post.next
            cur.next = pre
            tail.next = post
            cur = tail

        return dummy.next