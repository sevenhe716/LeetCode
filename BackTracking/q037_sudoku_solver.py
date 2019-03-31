# Time:  O(n)
# Space: O(1)

# 解题思路：
# 回溯应该是个可以尝试的思路，但是如果要减少回溯的次数，优化的方式应该是优先填充个数尽量多的集合，人类的解题方式也是如此
# 维护每一排，每一列，每一大格的剩余的索引


class Solution:
    # def test(self, *arg):
    #     x, y = arg[0], arg[1]
    #     c = x % 3 * 3 + y % 3
    #     r = x // 3 * 3 + y // 3
    #     return r, c
    #
    # def cal(self, r, c):
    #     # print('{},{}'.format(r, c))
    #     # print('{},{}'.format(r // 3 * 3 + c // 3, r % 3 * 3 + c % 3))
    #     # print('')
    #     return r // 3 * 3 + c // 3, r % 3 * 3 + c % 3

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row_index = [set() for _ in range(9)]
        col_index = [set() for _ in range(9)]
        box_index = [set() for _ in range(9)]

        row_remain = [set([i for i in range(1, 10)]) for _ in range(9)]
        col_remain = [set([i for i in range(1, 10)]) for _ in range(9)]
        box_remain = [set([i for i in range(1, 10)]) for _ in range(9)]

        index_queue = []  # 遍历顺序
        remain = 0

        def remove_index(r, c):
            nonlocal remain
            row_index[r].remove(c)
            col_index[c].remove(r)
            box_index[r // 3 * 3 + c // 3].remove(r % 3 * 3 + c % 3)
            remain -= 1

        def add_index(r, c):
            nonlocal remain
            row_index[r].add(c)
            col_index[c].add(r)
            box_index[r // 3 * 3 + c // 3].add(r % 3 * 3 + c % 3)
            remain += 1

        def add_num(r, c, v):
            row_remain[r].add(v)
            col_remain[c].add(v)
            box_remain[r // 3 * 3 + c // 3].add(v)

        def remove_num(r, c, v):
            row_remain[r].remove(v)
            col_remain[c].remove(v)
            box_remain[r // 3 * 3 + c // 3].remove(v)

        for r_i, row in enumerate(board):
            for c_i, v in enumerate(row):
                if v != '.':
                    num = int(v)
                    remove_num(r_i, c_i, num)
                else:
                    add_index(r_i, c_i)

        # 先创建一个较优的遍历顺序，按照这个顺序进行回溯
        while remain > 0:
            # 选择最可能的解
            min_r, min_c = -1, -1
            min_count = 30

            for r_i, rr in enumerate(row_index):
                for c_i in rr:
                    cur_count = 0
                    cur_count += len(rr)
                    cur_count += len(col_index[c_i])
                    cur_count += len(box_index[r_i // 3 * 3 + c_i // 3])

                    if cur_count < min_count:
                        min_count = len(rr)
                        min_r = r_i
                        min_c = c_i

                #
                # if 0 < len(rr) < min_count:
                #     min_count = len(rr)
                #     min_r = i
                #     min_c = next(iter(rr))

                # RNG based set
                # next(iter(s))
                # random.sample(s, 1)
                # for first_item in muh_set: break
            #
            # for i, cc in enumerate(col_index):
            #     if 0 < len(cc) < min_count:
            #         min_count = len(cc)
            #         min_c = i
            #         min_r = next(iter(cc))
            #
            # for i, bb in enumerate(box_index):
            #     if 0 < len(bb) < min_count:
            #         min_count = len(bb)
            #         x = i
            #         y = next(iter(bb))
            #         min_c = x % 3 * 3 + y % 3
            #         min_r = x // 3 * 3 + y // 3

            # 压栈
            index_queue.append((min_r, min_c))
            remove_index(min_r, min_c)

        find = False

        # 回溯法
        def solve(cur_index):
            nonlocal find
            if find:
                return

            if cur_index == len(index_queue):
                find = True
                return

            r_i, c_i = index_queue[cur_index]
            intersection = row_remain[r_i] & col_remain[c_i] & box_remain[r_i // 3 * 3 + c_i // 3]

            for num in intersection:
                # print('cur={}, r={}, c={}, nums={} num={}'.format(cur_index, r_i, c_i, intersection, num))

                remove_num(r_i, c_i, num)
                # print('remove {} {} {}'.format(r_i, c_i, v))
                board[r_i][c_i] = str(num)
                solve(cur_index + 1)
                add_num(r_i, c_i, num)
                if find:
                    return

            # print('backtracking')

        solve(0)


class Solution1:
    # easy-understanding version, not a efficient solution
    # optimize: use priority queue and bit-manipulation
    def solveSudoku(self, board):
        stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]

        def dfs():
            if not stack:
                return
            x, y = stack.pop()
            box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs()
                    if not stack:
                        return
            board[x][y] = "."
            stack.append((x, y))

        dfs()
