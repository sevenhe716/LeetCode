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
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        pre, post = None, head
        while post:
            post.next, pre, post = pre, post, post.next
        return pre
