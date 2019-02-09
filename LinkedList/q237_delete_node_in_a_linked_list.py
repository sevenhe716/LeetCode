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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 这种解法无法删除最后一个节点
        node.val, node.next = node.next.val, node.next.next
