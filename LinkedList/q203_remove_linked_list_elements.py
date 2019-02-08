# Time:  O(n)
# Space: O(1)

# 解题思路：
# 两种思路，1. 常规思路是删除对应节点，2. 用数组统计，重新赋值和截断


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # 删除指定节点
    def removeElements1(self, head: 'ListNode', val: 'int') -> 'ListNode':
        cur = dummy = ListNode(0)
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    # 批量修改节点值，并截断
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        vals = []
        dummy = ListNode(0)
        cur = dummy.next = head
        while cur:
            if cur.val != val:
                vals.append(cur.val)
            cur = cur.next

        cur = dummy
        for v in vals:
            cur.next.val = v
            cur = cur.next
        cur.next = None
        return dummy.next
