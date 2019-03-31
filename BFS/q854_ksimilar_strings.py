# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 尝试用链表解决，链表的思路是不对的，可以进行不相邻的交换，用链表交换次数很多
# 再尝试用贪心算法，优先交换二者都匹配成功的，再交换当前不在正确位置上的
# 贪心算法取不到最优解，只能尝试回溯或动态规划
# 回溯，还是遵循前面的规则，遍历所有的可能性，若已经超过了目前最少的步骤，则提前终止
# 优化思路：可以考虑memorized
from common import ListNode
from collections import Counter


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

    # backtracking
    def kSimilarity(self, A, B):
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
                    elif A[j] != b[j]:  # if A[j] == b[j], this swap also remain one mis-match, exclude this situation
                        pos.append(j)

            for k in pos:
                b[i], b[k] = b[k], b[i]
                backtracking(step + 1, i)
                b[i], b[k] = b[k], b[i]

        backtracking(0, 0)

        return min_step


class Solution1:
    # fastest 40ms
    def kSimilarity(self, A: str, B: str) -> int:
        def bfs(s, e):
            layer = [[s]]
            while True:
                next_layer = []
                while layer:
                    path = layer.pop()
                    curr = path[-1]
                    if (curr, e) in counter:
                        return path + [e]
                    for i in range(6):
                        if i not in path and (curr, i) in counter:
                            next_layer.append(path + [i])
                layer = next_layer

        counter = Counter()
        for i in range(len(A)):
            p, q = ord(A[i]) - 97, ord(B[i]) - 97
            if p != q:
                counter[(p, q)] += 1
        res = 0
        while counter:
            keys = list(counter.keys())
            best = [0] * 7
            for a, b in keys:
                path = bfs(b, a)
                if len(path) == 2:
                    best = path
                    break
                if len(best) > len(path):
                    best = path
            a, b = best[-1], best[0]
            path = bfs(b, a)
            res += len(path) - 1
            for i in range(len(path) - 1):
                if counter[(path[i], path[i + 1])] <= 1:
                    counter.pop((path[i], path[i + 1]))
                else:
                    counter[(path[i], path[i + 1])] -= 1
            if counter[(a, b)] > 1:
                counter[(a, b)] -= 1
            else:
                counter.pop((a, b))
        return res
