# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用链表实现加法运算
# 需要考虑的特殊情况(corner case)：
# 1. 其中一个链表已经遍历完成
# 2. 加法进位的问题

# Definition for singly-linked list.
from common import ListNode


class Solution:
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0           # 进位标记符
        head = ListNode(0)   # 标记用头节点，最终需要去掉，或在循环体内判断ListNode是否为None
        current = head

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:   # 参考答案用了divmod除法函数 carry, val = divmod(val, 10)
                val -= 10
                carry = 1
            else:
                carry = 0

            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(carry)

        return head.next


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l1.val is 0 and l1.next is None:
            return l2
        elif l2 is None or l2.val is 0 and l2.next is None:
            return l1

        head = cur = l1
        carry = 0

        while l1 and l2:
            # faster than divmod
            # add = carry + l1.val + l2.val
            # carry, l1.val = (1, add) if add > 9 else (0, add)
            carry, l1.val = divmod(carry + l1.val + l2.val, 10)
            cur, l1, l2 = l1, l1.next, l2.next

        if l2:
            cur.next = l2

        tail, cur = cur, cur.next   # tail用于记录cur的pre node

        while cur and carry == 1:
            carry, cur.val = divmod(carry + cur.val, 10)
            tail, cur = cur, cur.next

        if carry == 1:
            tail.next = ListNode(1)

        return head

# 快的核心是based on L1，减少了很多初始化ListNode的开销，但是不一定符合题意
class SolutionF:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or (l1.val is 0 and l1.next is None):
            return l2
        elif l2 is None or (l2.val is 0 and l2.next is None):
            return l1

        # let's always return a new list basing on l1, will return root finally
        # thus, no need to create a new link list or list node which will take some time and memory
        root = l1
        add = carrier = 0
        l_cur = None
        while l1 and l2:
            add = l1.val + l2.val + carrier
            # if ... else is much faster
            l1.val, carrier = (add - 10, 1) if add > 9 else (add, 0)
            l_cur = l1
            l1, l2 = l1.next, l2.next

        # In case l2 is longer than l1, to fully utilize the chracter of link list, connect the left l2 to l1
        if l2:
            l_cur.next = l2
        # the tail is going to be changed possibly with None
        possible_tail = l_cur
        l_cur = l_cur.next

        # same logic as before
        while l_cur:
            add = l_cur.val + carrier
            # if ... else is much faster
            l_cur.val, carrier = (add - 10, 1) if add > 9 else (add, 0)

            # the tail is going to be changed possibly with None
            possible_tail = l_cur
            l_cur = l_cur.next
        if carrier:
            # Actually we only create one node if possible
            possible_tail.next = ListNode(1)

        return root

    def addTwoNumbers1(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry /= 10
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0

        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first

    def addTwoNumbers3(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0

        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node

        return tolist(toint(l1) + toint(l2))

