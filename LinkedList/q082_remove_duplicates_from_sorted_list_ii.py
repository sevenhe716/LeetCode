# Time:  O(n)
# Space: O(1)

# 解题思路：
# 这道题的难点在于，不是删除重复的节点，而是把有重复的节点全部删除
# 两种思路，删除有重复值的节点，或者先遍历一遍，得到序列再统一赋值


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # 统计并统一赋值
    def deleteDuplicates1(self, head: 'ListNode') -> 'ListNode':
        # 添加哨兵节点
        dummy = ListNode(float('inf'))
        cur = dummy.next = head
        res, duplicated = [dummy.val], False
        while cur:
            if res[-1] == cur.val:
                duplicated = True
            else:
                if duplicated:
                    res[-1] = cur.val
                else:
                    res.append(cur.val)
                duplicated = False
            cur = cur.next
        if duplicated:
            res.pop()
        cur = dummy
        for v in res[1:]:
            cur.next.val = v
            cur = cur.next
        cur.next = None
        return dummy.next

    # 边遍历边删除
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        cur = dummy = ListNode(float('inf'))
        dummy.next = head
        while cur.next:
            check_node = cur
            duplicated = False
            while check_node.next.next and check_node.next.val == check_node.next.next.val:
                check_node = check_node.next
                duplicated = True
            if duplicated:
                cur.next = check_node.next.next
            else:
                cur = cur.next
        return dummy.next
