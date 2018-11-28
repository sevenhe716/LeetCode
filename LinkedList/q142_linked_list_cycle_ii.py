# Time:  O(n)
# Space: O(1)

# 解题思路：
# 假设环之前的长度为a，环的长度为b
# 先用快慢指针检测环，慢指针步长为1，快指针步长为2，计数检测到环的步数n，则二者步长之差则为2n-n=kb，即环的长度的整数倍
# 再次重头遍历链表，快指针比慢指针早出发n（即kb），且指针步长都为1，然后当快慢指针再次相遇时(经过m步)，则一定相遇在环的初始位置
# 因为m和m+kb必定在环的起始位置相遇，即m=a
# 边界条件，注意判断无环和环为空的特殊情况


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        count = 0
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            count = count + 1
            if fast is slow:
                break

        if not fast.next or not fast.next.next:
            return None

        fast, slow = head, head
        for _ in range(count):
            fast = fast.next

        while fast is not slow:
            fast, slow = fast.next, slow.next

        return fast
