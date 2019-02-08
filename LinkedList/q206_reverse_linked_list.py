# Time:  O(n)
# Space: O(1)

# 解题思路：
# 翻转链表或者更新值，翻转链表有迭代和递归两种写法


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # update values
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        values, cur = [], head
        while cur:
            values.append(cur.val)
            cur = cur.next
        values.reverse()
        cur = head
        for v in values:
            cur.val = v
            cur = cur.next
        return head

    # iteratively
    def reverseList1(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        pre, cur, post = None, head, head.next
        while post:
            cur.next = pre
            pre, cur, post = cur, post, post.next
        cur.next = pre
        return cur

    # recursively
    def reverseList2(self, head: 'ListNode') -> 'ListNode':
        def reverseListR(n1, n2):
            post = n2.next
            n2.next = n1
            return reverseListR(n2, post) if post else n2
        return reverseListR(None, head) if head else head

