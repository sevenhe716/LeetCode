# Time:  O(knlog(k))
# Space: O(k)

# 解题思路：
# 用有序list维护当前指针，这样插入新节点的时间复杂度降为O(log(k))，移除节点(取出当前最小的元素)的时间复杂度降为O(1)
# 统计所有链表的总长度，用于循环的终止条件

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
from common import ListNode


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        count = 0

        for l in lists:
            node = l
            while node:
                node = node.next
                count += 1

        order_headers = sorted([l for l in lists if l], key=lambda x: x.val)

        while count > 0:
            node = order_headers.pop(0)  # pop the minimum
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                lo, hi = 0, len(order_headers)  # binary search
                while lo < hi:
                    mid = (lo + hi) // 2
                    if order_headers[mid].val < node.val:
                        lo = mid + 1
                    else:
                        hi = mid
                order_headers.insert(lo, node)
            count -= 1

        return dummy.next


# Merge two by two solution.
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]


# 分治法
# Time:  O(nlogk)
# Space: O(logk)
# Divide and Conquer solution.
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2),
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)


# heapq 基于堆的优先排序算法，堆的逻辑结构就是完全二叉树，并且二叉树中父节点的值小于等于该节点的所有子节点的值。
# 这种实现可以使用 heap[k] <= heap[2k+1] 并且 heap[k] <= heap[2k+2]
class SolutionF:
    def mergeKLists(self, lists):
        import heapq

        pre = cur = ListNode(0)

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))  # 按照list.val来排序

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return pre.next


# 直接把所有元素放到list里排序，还真是简单粗暴
class SolutionF2:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodelist = []
        for head in lists:
            current = head
            while current:
                nodelist.append(current)
                current = current.next

        nodelist.sort(key=lambda x: x.val)

        for i in range(len(nodelist) - 1):
            nodelist[i].next = nodelist[i + 1]
        if not nodelist:
            return None

        else:
            return nodelist[0]

    def mergeKLists2(self, lists):
        def gen(node):
            while node:
                yield node.val, node
                node = node.next

        dummy = last = ListNode(None)
        for _, last.next in heapq.merge(*map(gen, lists), key=lambda x: x[0]):
            last = last.next
        return dummy.next

    def mergeKLists3(self, lists):
        # should use wrapper class to override __lt__
        class Wrapper:
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, Wrapper(l))
        while q:
            node = q[0].node
            point.next = node
            point = point.next
            node = node.next
            if node:
                # fast version than pop & push
                heapq.heapreplace(q, Wrapper(node))
            else:
                heapq.heappop(q)
        return head.next
