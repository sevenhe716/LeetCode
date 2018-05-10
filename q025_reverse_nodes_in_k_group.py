# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用一个指针先往后找K个节点，看是否还有K个长度，然后将这K个元素进行链表反转，需要注意的是，将原来的头节点与新的尾节点相连

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        cur = dummy = ListNode(0)
        tail = dummy.next = head

        while tail:
            for i in range(k):
                if not tail:
                    return dummy.next
                tail = tail.next

            k_head = cur.next
            cur.next = self.reverse(k_head, k-1)
            cur = k_head

        return dummy.next

    # ensure head is not None and length >= k, return new head
    def reverse(self, head, k):
        n1 = head
        n2 = n1.next

        while k > 0:
            next_node = n2
            n2 = n2.next
            next_node.next = n1
            n1 = next_node
            k -= 1

        head.next = n2
        return n1


class Solution1:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head

        cur, cur_dummy = head, dummy
        length = 0

        while cur:
            next_cur = cur.next
            length = (length + 1) % k

            if length == 0:
                next_dummy = cur_dummy.next
                self.reverse(cur_dummy, cur.next)
                cur_dummy = next_dummy

            cur = next_cur

        return dummy.next

    def reverse(self, begin, end):
            first = begin.next
            cur = first.next

            while cur != end:
                first.next = cur.next
                cur.next = begin.next
                begin.next = cur
                cur = first.next

class SolutionF:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):      # 借鉴
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
#  multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
