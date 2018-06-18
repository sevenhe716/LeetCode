# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 尝试用链表解决，链表的思路是不对的，可以进行不相邻的交换，用链表交换次数很多
# 再尝试用贪心算法，优先交换二者都匹配成功的，再交换当前不在正确位置上的
# 贪心算法取不到最优解，只能尝试回溯或动态规划
# 回溯，还是遵循前面的规则，遍历所有的可能性，若已经超过了目前最少的步骤，则提前终止
# 优化思路：可以考虑memorized
from common import ListNode


class Solution:
    # 链表
    def kSimilarity1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        dummy1, dummy2 = ListNode('s'), ListNode('s')
        cur1, cur2 = dummy1, dummy2

        for c in zip(A, B):
            cur1.next, cur2.next = ListNode(c[0]), ListNode(c[1])
            cur1, cur2 = cur1.next, cur2.next

        cur1, cur2 = dummy1, dummy2
        step = 0
        while cur1.next:
            cur2_1 = cur2
            while cur1.next.val != cur2.next.val:
                cur2 = cur2.next
                step += 1

            if cur2_1 != cur2:
                tmp = cur2.next  # python的多重赋值是否可以简化？
                cur2.next = cur2.next.next
                tmp.next = cur2_1.next
                cur2_1.next = tmp
                cur2 = cur2_1

            cur1, cur2 = cur1.next, cur2.next

        return step

    # greedy
    def kSimilarity2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        step, i, n = 0, 0, len(A)
        a, b = list(A), list(B)

        print(a)
        print(b)
        print()

        while i < n:
            if a[i] != b[i]:
                c = a[i]
                for j in range(i + 1, n):
                    if b[j] == c:
                        if a[j] == b[i]:
                            k = j
                            break
                        elif a[j] != b[j]:
                            k = j

                b[i], b[k] = b[k], b[i]
                print(a)
                print(b)
                print()
                step += 1

            i += 1

        return step

    # backtracking:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = len(A)
        b = list(B)
        min_step = 2147483647

        def backtracking(step, i):
            nonlocal min_step
            if step >= min_step:  # exceed min_step, early stop
                return

            while i < n and A[i] == b[i]:
                i += 1

            if i == n:
                min_step = min(step, min_step)
                return

            pos = []
            for j in range(i + 1, n):
                if b[j] == A[i]:
                    # should be the optimal swap, match two pairs in one swap,
                    # even if have multiple A[j]==b[i], we can just pick any one
                    if A[j] == b[i]:
                        pos = [j]
                        break
                    elif A[j] != b[
                        j]:  # if A[j] == b[j], this swap also remain one mis-match, exclude this situation
                        pos.append(j)

            for k in pos:
                b[i], b[k] = b[k], b[i]
                backtracking(step + 1, i)
                b[i], b[k] = b[k], b[i]

        backtracking(0, 0)

        return min_step


class Solution1:
    # BFS:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A == B:
            return 0

        def swap(s, i, j):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            return ''.join(s_list)

        vis = set()
        q = []
        vis.add(A)
        q.append(A)
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                s = q.pop(0)
                i = 0
                while s[i] == B[i]: i += 1
                for j in range(i + 1, len(s)):
                    if s[j] == B[j] or s[i] != B[j]: continue
                    temp = swap(s, i, j)
                    if temp == B: return res
                    if temp not in vis:
                        q.append(temp)
                    vis.add(temp)

        return res