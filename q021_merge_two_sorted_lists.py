# Time:  O(n)
# Space: O(1)

# 解题思路：
# 默认是可以破坏原list（原地）
# 使用一个cur指针，及dummy头结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # 原地合并
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        n1 = ListNode(0)        # 优化：先找到小的头节点，可以无需添加dummy节点
        n1.next, n2 = l1, l2
        head = n1

        while n1.next and n2:
            if n1.next.val <= n2.val:
                n1 = n1.next
            else:
                p = n2
                n2 = n2.next
                p.next = n1.next
                n1.next = p
                n1 = n1.next

        if n2:
            n1.next = n2

        return head.next


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2            # 这个写法很简洁，借鉴
        return dummy.next


class SolutionF:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dumy = ListNode(0)
        cur = dumy
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
            elif l1:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return dumy.next

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
# nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
