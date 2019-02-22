# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 考虑用回溯，每一步有三种操作方式，add delete或replace
# 优化思路：当步骤已经超过当前最小步骤时，可以提前终止
# 特殊情况，如果一端已经到末尾，则只能添加或删除，步骤直接加差值
# 缓存之前遍历过的结果
# 动态规划思路更佳
from common import print_matrix


class Solution:
    # backtracking
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_step = len(word1) + len(word2)

        def backtracking(w1, w2, index, step):
            """
            :type w1: list
            :type w2: list
            :type index: int
            :type step: int
            """
            nonlocal min_step

            l1, l2 = len(w1), len(w2)

            if step + abs(l2 - l1) >= min_step:  # 提前终止
                return

            if index >= l1 and index >= l2:
                min_step = min(min_step, step)
                return

            if index >= l1 or index >= l2:
                step += abs(l2 - l1)
                min_step = min(min_step, step)
                return

            if w1[index] == w2[index]:
                backtracking(w1, w2, index + 1, step)
            else:
                c = w1[index]
                w1[index] = w2[index]
                backtracking(w1, w2, index + 1, step + 1)
                w1[index] = c

                w1.insert(index, w2[index])
                backtracking(w1, w2, index + 1, step + 1)
                w1.pop(index)

                c = w1.pop(index)
                backtracking(w1, w2, index, step + 1)
                w1.insert(index, c)

        backtracking(list(word1), list(word2), 0, 0)

        return min_step

    # backtracking, with memorization
    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        int32_max = 2147483647
        min_step = len(word1) + len(word2)
        cache = {}

        def backtracking(w1, w2, index, step):
            """
            :type w1: list
            :type w2: list
            :type index: int
            :type step: int
            """
            nonlocal min_step

            l1, l2 = len(w1), len(w2)

            if step + abs(l2 - l1) >= min_step:  # 提前终止
                cache[(''.join(w1), ''.join(w2))] = int32_max
                return int32_max

            if index >= l1 and index >= l2:
                min_step = min(min_step, step)
                cache[(''.join(w1), ''.join(w2))] = step
                # print('stop, step={}'.format(step))
                # print()
                return step

            if index >= l1 or index >= l2:
                step += abs(l2 - l1)
                min_step = min(min_step, step)
                cache[(''.join(w1), ''.join(w2))] = step
                # print('stop, step={}'.format(step))
                # print()
                return step

            res = int32_max

            if w1[index] == w2[index]:
                # print('go on index={}, w1={}, w2={}'.format(index, w1, w2))
                return backtracking(w1, w2, index + 1, step)
            else:
                c = w1[index]
                # print('replace index={}, w1={}, w2={}, step={}'.format(index, w1, w2, step))
                w1[index] = w2[index]
                key = (''.join(w1), ''.join(w2))
                if key in cache:
                    cur = cache[key]
                else:
                    cur = backtracking(w1, w2, index + 1, step + 1)

                res = min(cur, res)
                w1[index] = c

                # print('insert index={}, w1={}, w2={}, step={}'.format(index, w1, w2, step))
                w1.insert(index, w2[index])
                key = (''.join(w1), ''.join(w2))
                if key in cache:
                    cur = cache[key]
                else:
                    cur = backtracking(w1, w2, index + 1, step + 1)

                res = min(cur, res)
                w1.pop(index)

                # print('delete index={}, w1={}, w2={}, step={}'.format(index, w1, w2, step))
                c = w1.pop(index)
                key = (''.join(w1), ''.join(w2))
                if key in cache:
                    cur = cache[key]
                else:
                    backtracking(w1, w2, index, step + 1)

                res = min(cur, res)
                w1.insert(index, c)

                return res

        backtracking(list(word1), list(word2), 0, 0)

        return min_step

    # dynamic programming
    # 优化：只需要访问到前一位置，无需存储m*n的空间
    def minDistance4(self, word1: 'str', word2: 'str') -> 'int':
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        m, n = len(word1), len(word2)
        # 状态定义：当前最短编辑距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 注意边界条件定义，多构造一个初始维度，用于边界条件合并
        for i in range(0, m + 1):
            dp[i][0] = i
        for j in range(0, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 状态转移方程：edit+remove+add
                dp[i][j] = min(dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1,
                               dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        print_matrix(dp)
        return dp[-1][-1]

    # dynamic programming
    # 优化：只需要访问到前一位置，无需存储m*n的空间
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        # if len(word1) > len(word2):
        #     word1, word2 = word2, word1
        #
        # if not word1:
        #     return len(word2)

        m, n = len(word1), len(word2)

        # 状态定义：当前最短编辑距离
        dp = [[0] * (m + 1) for _ in range(2)]

        # 注意边界条件定义，多构造一个初始维度，用于边界条件合并
        for i in range(0, m + 1):
            dp[0][i] = i

        cur = 1
        for i in range(1, n + 1):
            dp[cur][0] = i
            for j in range(1, m + 1):
                # 状态转移方程：当dp[i][j]字符匹配时，dp[i-1][j-1]是最短距离，无需比较添加和删除
                if word1[j - 1] == word2[i - 1]:
                    dp[cur][j] = dp[1 - cur][j - 1]
                else:
                    dp[cur][j] = 1 + min(dp[1 - cur][j - 1], dp[1 - cur][j], dp[cur][j - 1])
            cur = 1 - cur
        return dp[1 - cur][-1]
