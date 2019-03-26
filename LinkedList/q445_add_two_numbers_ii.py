# Time:  O(n)
# Space: O(n)

# Ideas:
# a simple solution is change the value in the list, and traverse and record it
# if not use extra space or reverse, it has to traverse over and over again


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        nums1, nums2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            nums1 = nums1 * 10 + cur1.val
            cur1 = cur1.next
        while cur2:
            nums2 = nums2 * 10 + cur2.val
            cur2 = cur2.next

        nums1 += nums2
        if nums1 == 0:
            return l1

        dummy = ListNode(0)
        # don't allow to modify the list, so has to create new ListNode
        while nums1 > 0:
            nums1, digit = divmod(nums1, 10)
            cur = ListNode(digit)
            dummy.next, cur.next = cur, dummy.next
        return dummy.next
