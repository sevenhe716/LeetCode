# Time:  O(n)
# Space: O(1)

# Ideas:
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a, len_b = 0, 0
        cur_a, cur_b = headA, headB
        while cur_a:
            cur_a = cur_a.next
            len_a += 1
        while cur_b:
            cur_b = cur_b.next
            len_b += 1

        cur_a, cur_b = headA, headB
        if len_a > len_b:
            for i in range(len_a - len_b):
                cur_a = cur_a.next
        else:
            for i in range(len_b - len_a):
                cur_b = cur_b.next

        while cur_a and cur_b:
            if cur_a == cur_b:
                return cur_a
            cur_a, cur_b = cur_a.next, cur_b.next

        return None



