# Time:  O(n)
# Space: O(n)

# 解题思路：
# 默认原链表是可破坏性的，因为是有序删除，所以可以先统计成一个列表，再赋值后截断，空间换时间

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        # 巧妙地借用python的成员变量动态声明
        self.next, cur = head, self
        nums = [self.next.val]

        while cur.next:
            if cur.next.val != nums[-1]:
                nums.append(cur.next.val)
            cur = cur.next

        cur = self
        for num in nums:
            cur.next.val = num
            cur = cur.next

        cur.next = None
        return head


# 直接边遍历边删除，但速度更慢
class Solution1:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next  # skip duplicated node
            cur = cur.next  # not duplicate of current node, move to next node
        return head