# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用链表实现加法运算
# 需要考虑的特殊情况：
# 1. 其中一个链表已经遍历完成
# 2. 加法进位的问题

# Definition for singly-linked list.
from common import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0           # 进位标记符
        head = ListNode(0)   # 标记用头节点，最终需要去掉，或在循环体内判断ListNode是否为None
        current = head

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:   # 参考答案用了divmod除法函数 carry, val = divmod(val, 10)
                val -= 10
                carry = 1
            else:
                carry = 0

            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(carry)

        return head.next


# 快的核心是based on L1，减少了很多初始化ListNode的开销，但是不一定符合题意
class SolutionF:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or (l1.val is 0 and l1.next is None):
            return l2
        elif l2 is None or (l2.val is 0 and l2.next is None):
            return l1

        # let's always return a new list basing on l1, will return root finally
        # thus, no need to create a new link list or list node which will take some time and memory
        root = l1
        add = carrier = 0
        l_cur = None
        while l1 and l2:
            add = l1.val + l2.val + carrier
            # if ... else is much faster
            l1.val, carrier = (add - 10, 1) if add > 9 else (add, 0)
            l_cur = l1
            l1, l2 = l1.next, l2.next

        # In case l2 is longer than l1, to fully utilize the chracter of link list, connect the left l2 to l1
        if l2:
            l_cur.next = l2
        # the tail is going to be changed possibly with None
        possible_tail = l_cur
        l_cur = l_cur.next

        # same logic as before
        while l_cur:
            add = l_cur.val + carrier
            # if ... else is much faster
            l_cur.val, carrier = (add - 10, 1) if add > 9 else (add, 0)

            # the tail is going to be changed possibly with None
            possible_tail = l_cur
            l_cur = l_cur.next
        if carrier:
            # Actually we only create one node if possible
            possible_tail.next = ListNode(1)

        return root

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
