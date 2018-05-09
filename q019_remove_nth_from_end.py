# Time:  O(n)
# Space: O(1)

# 解题思路：
# 双指针同时遍历即可，相差n
# n保证有效，无需处理特殊情况，还是需要考虑只有一个节点的情况，比较简单的办法是增加一个dummy头节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # n保证有效，无需处理特殊情况，无需处理空list或n越界
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        root = ListNode(0)
        root.next = head
        p1 = p2 = root

        for i in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        # p2.next = p2.next.next if p2.next else None
        p2.next = p2.next.next      # 加了dummy就不需要判断是否为空

        return root.next


class Solution1:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next


class SolutionF:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.next = head
        h1 = h2 = self
        while h1.next:
            if n:
                n = n-1
            else:
                h2 = h2.next
            h1 = h1.next
        h2.next = h2.next.next
        return self.next


# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
