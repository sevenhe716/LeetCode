# Time:  O(n)
# Space: O(1)

# 解题思路：
# 插入排序的链表版本，两种思路，修改节点或者修改值
# 思路优化：更好的思路是直接维护两个新的链表，分别存储小于和大于的数据，然后再串联起来


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import ListNode


class Solution:
    # 修改节点
    # 双指针，一个指向比目标大的替换位置，一个指向比目标小的替换位置，利用链表的优势，分别遍历可减少遍历次数
    def partition(self, head: 'ListNode', x: int) -> 'ListNode':
        if not head:
            return None
        greater = dummy = ListNode(None)
        dummy.next, less = head, None

        while True:
            # 寻找比x大的节点
            while greater.next.val < x:
                greater = greater.next
                if not greater.next:
                    return dummy.next

            # 需要保证less在greater之后，所以需要先进行一次初始化
            if not less:
                less = greater.next

            if not less.next:
                return dummy.next

            # 寻找比x小的节点
            while less.next.val >= x:
                less = less.next
                if not less.next:
                    return dummy.next

            greater.next, less.next, greater.next.next = less.next, less.next.next, greater.next

            greater = greater.next
            if not greater:
                return dummy.next

class Solution1:
    def partition(self, head: 'ListNode', x: int) -> 'ListNode':
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next
