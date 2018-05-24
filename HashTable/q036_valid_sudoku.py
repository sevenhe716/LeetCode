# Time:  O(n)
# Space: O(1)

# 解题思路：
# 根据数组的row column sub-box三条规则验证即可，这里使用二维数组来维护
# 优化思路：使用字典会更快，无需遍历完，一旦检测到有重复的情况，直接返回失败


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # import numpy as np
        # row_counters = np.zeros((9, 9))
        # col_counters = np.zeros((9, 9))
        # box_counters = np.zeros((9, 9))

        row_counters = [[0 for _ in range(9)] for _ in range(9)]
        col_counters = [[0 for _ in range(9)] for _ in range(9)]
        box_counters = [[0 for _ in range(9)] for _ in range(9)]

        for r_i, row in enumerate(board):
            for c_i, v in enumerate(row):
                if v.isdigit():
                    d_v = int(v) - 1
                    row_counters[r_i][d_v] += 1
                    col_counters[c_i][d_v] += 1
                    box_counters[c_i // 3 * 3 + r_i // 3][d_v] += 1

        for i in range(9):
            if max(row_counters[i]) > 1 or max(col_counters[i]) > 1 or max(box_counters[i]) > 1:
                return False

        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row_counters = [{} for _ in range(9)]
        col_counters = [{} for _ in range(9)]
        box_counters = [{} for _ in range(9)]

        for r_i, row in enumerate(board):
            for c_i, v in enumerate(row):
                if v.isdigit():
                    num = int(v) - 1
                    box_i = r_i // 3 * 3 + c_i // 3
                    if num not in row_counters[r_i] and num not in col_counters[c_i] \
                            and num not in box_counters[box_i]:
                        row_counters[r_i][num] = 1
                        col_counters[c_i][num] = 1
                        box_counters[box_i][num] = 1
                    else:
                        return False

        return True
