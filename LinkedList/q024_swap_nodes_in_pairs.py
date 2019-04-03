# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用指针交换next节点即可，需要注意的是边界条件的判断

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # already contain this situation
        # if not head or not head.next:
        #     return head

        n1 = dummy = ListNode(0)
        n2 = n1.next = head

        while n2 and n2.next:
            n3 = n2
            n2 = n2.next
            n3.next = n2.next
            n1.next = n2
            n2.next = n3

            n1 = n2.next
            n2 = n1.next

        return dummy.next


class SolutionF:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumy = ListNode(0)
        dumy.next = head
        cur = dumy
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = node1.next
            nxt = node2.next

            cur.next = node2
            node2.next = node1
            node1.next = nxt

            cur = node1
        return dumy.next
