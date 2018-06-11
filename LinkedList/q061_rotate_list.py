# Time:  O(n)
# Space: O(1)

# 解题思路：
# k需要取模，以减少遍历次数，所以需要先求出链表长度，不能在one-pass中完成
# 优化思路：不需要dummy node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode

class Solution:
    def rotateRight1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        count = 0
        dummy = ListNode(0)
        dummy.next = head       # 无需dummy node
        cur = dummy

        while cur.next:
            count += 1
            cur = cur.next

        k %= count
        if k == 0:
            return head

        cur = dummy
        for _ in range(count - k):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        dummy.next = new_head
        while new_head.next:
            new_head = new_head.next

        new_head.next = head        # 可以在计算长度时就赋值，减少遍历次数

        return dummy.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        count = 1
        cur = head
        while cur.next:
            count += 1
            cur = cur.next

        k %= count
        if k == 0:
            return head

        cur.next = head
        cur = head
        for _ in range(count - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head


