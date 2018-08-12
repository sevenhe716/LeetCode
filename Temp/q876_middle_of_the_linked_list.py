# Time:  O(n)
# Space: O(1)

# 解题思路：
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n1, n2 = head, head

        while n2:
            n2 = n2.next
            if n2:
                n2 = n2.next
            else:
                break
            n1 = n1.next

        return n1
