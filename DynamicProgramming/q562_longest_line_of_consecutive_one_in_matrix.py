# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 对于斜边，找到边界然后验证范围，一个优化的点是，如果斜边的总长度小于等于当前最大值，则直接跳过
# 比较无脑的解法是不计算size，直接越界后终止
# 我的解法虽然繁琐，但执行效率很高，有很多提前终止循环的判断，额外的空间复杂度也很低
import collections


class Solution:
    def longestLine(self, M: 'List[List[int]]') -> int:
        if not M or not M[0]:
            return 0
        m, n, self.res = len(M), len(M[0]), 0
        # 短轴
        s = min(m, n)

        # check row
        def check_row():
            for i in range(m):
                count = 0
                for j in range(n):
                    if M[i][j] == 1:
                        count += 1
                    else:
                        self.res = max(self.res, count)
                        count = 0
                self.res = max(self.res, count)

        # check column
        def check_col():
            for i in range(n):
                count = 0
                for j in range(m):
                    if M[j][i] == 1:
                        count += 1
                    else:
                        self.res = max(self.res, count)
                        count = 0
                self.res = max(self.res, count)

        # 先查长轴
        if n >= m:
            check_row()
            # 如果大于等于短轴可以直接跳过后续
            if self.res >= s:
                return self.res
            check_col()
        else:
            check_col()
            if self.res >= s:
                return self.res
            check_row()

        if self.res >= s:
            return self.res

        # check diagonal
        for i, j in [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]:
            # 计算斜线的长度
            size = min(m - i, n - j)
            # 长度小于等于res的斜线可以直接跳过
            if size <= self.res:
                continue
            count = 0
            for k in range(size):
                if M[i + k][j + k] == 1:
                    count += 1
                else:
                    self.res = max(self.res, count)
                    count = 0
            self.res = max(self.res, count)

        if self.res >= s:
            return self.res

        # check anti-diagonal
        for i, j in [(i, n - 1) for i in range(m)] + [(0, j) for j in range(n - 1)]:
            size = min(m - i, n - m + j + 1)
            if size <= self.res:
                continue
            count = 0
            for k in range(size):
                if M[i + k][j - k] == 1:
                    count += 1
                else:
                    self.res = max(self.res, count)
                    count = 0
            self.res = max(self.res, count)

        return self.res


class Solution1:
    # StefanPochmann大神的解法，简洁但效率和空间复杂度要差一些
    def longestLine1(self, M: 'List[List[int]]') -> int:
        maxlen = 0
        currlen = collections.Counter()
        for i, row in enumerate(M):
            for j, a in enumerate(row):
                # 借鉴：添加fractions，用作同一个dict中区分
                for key in i, j + .1, i + j + .2, i - j + .3:
                    # 两种情况用乘法即可合并
                    currlen[key] = (currlen[key] + 1) * a
                    # 每次都进行最大值比较
                    maxlen = max(maxlen, currlen[key])
        return maxlen

    # fastest, 一个循环中完成遍历
    def longestLine2(self, M: 'List[List[int]]') -> int:
        if not M or not M[0]:
            return 0

        rows, cols = len(M), len(M[0])

        ver = [0] * cols
        dia = [0] * (cols + 2)
        anti_dia = [0] * (cols + 2)

        max_count = 0
        for row in range(rows):
            hor = 0
            temp_dia = [0] * (cols + 2)
            temp_anti_dia = [0] * (cols + 2)
            for col in range(cols):
                if M[row][col] == 0:
                    ver[col] = 0
                    temp_dia[col + 1] = 0
                    temp_anti_dia[col + 1] = 0
                    hor = 0
                else:
                    hor += 1
                    ver[col] += 1
                    temp_dia[col + 1] = dia[col] + 1
                    temp_anti_dia[col + 1] = anti_dia[col + 2] + 1
                    max_count = max(max_count, hor, ver[col], temp_dia[col + 1], temp_anti_dia[col + 1])
            dia, anti_dia = temp_dia, temp_anti_dia
        return max_count

    # 3D DP
    def longestLine3(self, M: 'List[List[int]]') -> int:
        if len(M) == 0:
            return 0

        dp = [[[0, 0, 0, 0] for _ in range(len(M[0]))] for _ in range(len(M))]
        max_len = 0
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 1:
                    dp[row][col][0] = dp[row][col - 1][0] + 1 if col > 0 else 1
                    dp[row][col][1] = dp[row - 1][col][1] + 1 if row > 0 else 1
                    dp[row][col][2] = dp[row - 1][col - 1][2] + 1 if row > 0 and col > 0 else 1
                    dp[row][col][3] = dp[row - 1][col + 1][3] + 1 if row > 0 and col < len(M[0]) - 1 else 1
                    max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])

        return max_len

    # 压缩为2D DP
    def longestLine4(self, M: 'List[List[int]]') -> int:
        if len(M) == 0:
            return 0

        dp = [[0, 0, 0, 0] for _ in range(len(M[0]))]
        max_len = 0
        for i in range(len(M)):
            old = 0
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    dp[j][0] = dp[j - 1][0] + 1 if j > 0 else 1
                    dp[j][1] = dp[j][1] + 1 if i > 0 else 1
                    # diagonal需要额外缓存上一个节点，因为会被覆盖
                    prev = dp[j][2]
                    dp[j][2] = old + 1 if i > 0 and j > 0 else 1
                    old = prev
                    dp[j][3] = dp[j + 1][3] + 1 if i > 0 and j < len(M[0]) - 1 else 1
                    max_len = max(max_len, dp[j][0], dp[j][1], dp[j][2], dp[j][3])
                else:
                    # 由于是重用，需要重置原状态
                    old = dp[j][2]
                    dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0
        return max_len