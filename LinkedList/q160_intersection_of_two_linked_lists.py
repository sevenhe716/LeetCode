# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 统计两链表长度之差，然后长链表先开始走差值步，然后判断是否有相同的节点
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_A, len_B = 0, 0
        node_A, node_B = headA, headB
        while node_A:
            len_A += 1
            node_A = node_A.next
        while node_B:
            len_B += 1
            node_B = node_B.next

        long_node, short_node = (headA, headB) if len_A >= len_B else (headB, headA)

        for _ in range(abs(len_A - len_B)):
            long_node = long_node.next

        while long_node != short_node:
            long_node = long_node.next
            short_node = short_node.next

        return long_node