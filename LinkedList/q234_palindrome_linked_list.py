# Time:  O(n)
# Space: O(1)

# 解题思路：
# 要求时间复杂度O(n)，空间复杂度O(1)，有个比较trick的做法是用str来存储，不知是否符合题意，MLE了
# 翻转半个链表再比较即可


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Memory Limit Exceed
    def isPalindrome1(self, head: 'ListNode') -> 'bool':
        val1, val2 = '', ''
        while head:
            val1 = val1 + ' ' + str(head.val)
            val2 = str(head.val) + ' ' + val2
            head = head.next

        return val1[1:] == val2[:-1]

    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if not head or not head.next:
            return True
        count, cur = 0, head
        while cur:
            cur = cur.next
            count += 1

        pre, cur, post = None, head, head.next
        for _ in range(count // 2):
            cur.next = pre
            pre, cur, post = cur, post, post.next
        head.next = cur

        slow = pre
        fast = cur.next if count % 2 else cur

        for _ in range(count // 2):
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next

        return True


# 代码精炼优美，值得学习
class Solution1:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        check = None
        slow = fast = head
        # 指针遍历与前半链表翻转同时完成
        while fast and fast.next:
            fast = fast.next.next
            check, check.next, slow = slow, check, slow.next
        # 解决长度的奇偶问题
        if fast:
            slow = slow.next
        while slow and slow.val == check.val:
            slow = slow.next
            check = check.next
        return not check        # 是否抵达终点
