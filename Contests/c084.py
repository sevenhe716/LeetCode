
class Solution1:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in A:
            row.reverse()
            for i, v in enumerate(row):
                row[i] = 1 - v

        return A


class Solution2:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        from itertools import count

        s_list = list(S)

        # 不能这样排序，因为sources和targets可能有重复的情况
        # src_index_dict = {sources[i]: k for i, k in enumerate(indexes)}
        # tar_index_dict = {targets[i]: k for i, k in enumerate(indexes)}

        # sources = sorted(sources, key=lambda x: src_index_dict[x])
        # targets = sorted(targets, key=lambda x: tar_index_dict[x])

        src_dict = {k: list(sources[i]) for i, k in enumerate(indexes)}
        tar_dict = {k: list(targets[i]) for i, k in enumerate(indexes)}

        indexes.sort()

        # src_list = [list(s) for s in sources]
        # tar_list = [list(t) for t in targets]

        for i in range(len(indexes))[::-1]:
            start = indexes[i]
            end = start + len(src_dict[start])
            if s_list[start:end] == src_dict[start]:
                s_list = s_list[:start] + tar_dict[start] + s_list[end:]

        return ''.join(s_list)


class SolutionF(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            if all(i + k < len(S) and S[i + k] == x[k] for k in range(len(x))):
                S[i:i + len(x)] = list(y)

        return "".join(S)

    def findReplaceStringOneLine(self, S, indexes, sources, targets):
        from functools import reduce

        # tp = (i, s, t)
        return reduce(lambda S, tp: S[:tp[0]] + tp[2] + S[tp[0] + len(tp[1]):] if S[tp[0]:tp[0] + len(tp[1])] == tp[1] else S,
                      sorted(zip(indexes, sources, targets), reverse=True), S)


class Solution3:
    def largestOverlap1(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        if not A:
            return 0

        row_count = len(A[0])
        col_count = len(A)
        max_count = 0

        for i in range(row_count):
            for row in A:
                head = row[0]
                for row_i in range(1, row_count):
                    row[row_i - 1] = row[row_i]
                row[-1] = head

            for j in range(col_count):
                head_row = A[0]
                for col_i in range(1, col_count):
                    A[col_i - 1] = A[col_i]
                A[-1] = head_row

                # Check(A, B)
                count = 0

                for r in range(row_count):
                    for c in range(col_count):
                        if A[c][r] + B[c][r] == 2:
                            count += 1

                if count > max_count:
                    max_count = count

        return max_count

    def calcOverlap(self, A, B, max_count):
        count = 0
        for c in range(len(A)):
            for r in range(len(A[0])):
                if A[c][r] + B[c][r] == 2:
                    count += 1

        if count > max_count:
            max_count = count

        return max_count

    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        if not A:
            return 0

        row_count = len(A[0])
        col_count = len(A)
        max_count = 0

        import copy
        _A = copy.deepcopy(A)

        max_count = self.calcOverlap(_A, B, max_count)

        for i in range(row_count):
            # left
            for row in _A:
                for row_i in range(1, row_count):
                    row[row_i - 1] = row[row_i]
                row[-1] = 0

            max_count = self.calcOverlap(_A, B, max_count)

            # up
            for j in range(col_count):
                for col_i in range(1, col_count):
                    _A[col_i - 1] = _A[col_i]
                _A[-1] = [0, ] * len(_A[0])

                max_count = self.calcOverlap(_A, B, max_count)

        _A = copy.deepcopy(A)

        for i in range(row_count):
            # right
            for row in _A:
                for row_i in range(1, row_count):
                    row[row_i] = row[row_i - 1]
                row[0] = 0

            max_count = self.calcOverlap(_A, B, max_count)

            # up
            for j in range(col_count):
                for col_i in range(1, col_count):
                    _A[col_i - 1] = _A[col_i]
                _A[-1] = [0, ] * len(_A[0])

                max_count = self.calcOverlap(_A, B, max_count)

        _A = copy.deepcopy(A)

        for i in range(row_count):
            for row in _A:
                for row_i in range(1, row_count):
                    row[row_i] = row[row_i - 1]
                row[0] = 0

            max_count = self.calcOverlap(_A, B, max_count)

            for j in range(col_count):
                for col_i in range(1, col_count):
                    _A[col_i] = _A[col_i - 1]
                _A[0] = [0, ] * len(_A[0])

                max_count = self.calcOverlap(_A, B, max_count)

        _A = copy.deepcopy(A)

        for i in range(row_count):
            for row in _A:
                for row_i in range(1, row_count):
                    row[row_i - 1] = row[row_i]
                row[-1] = 0

            max_count = self.calcOverlap(_A, B, max_count)

            for j in range(col_count):
                for col_i in range(1, col_count):
                    _A[col_i] = _A[col_i - 1]
                _A[0] = [0, ] * len(_A[0])

                max_count = self.calcOverlap(_A, B, max_count)

        return max_count

    # def printA(self, A):
    #     for row in A:
    #         print(' '.join(str(row)))
    #     print('')


class Solution:
    def sumOfDistancesInTree1(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # dp
        dists = [[-1 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dists[i][i] = 0

        for edge in edges:
            dists[edge[0]][edge[1]] = dists[edge[1]][edge[0]] = 1

        while any(dists[i][j] < 0 for i in range(N) for j in range(N)):
            for dist_row in dists:
                for i in range(N-1):
                    for j in range(N):
                        if dists[i][j] < 0 and dist_row[i] > 0 and dist_row[j] > 0:
                            dists[i][j] = dists[j][i] = dist_row[i] + dist_row[j]

        sums = [0] * N
        for i in range(N):
            for j in range(N):
                sums[i] += dists[i][j]

        return sums

    # 解题思路：
    # 由于是全连通树（无环），从一个端点出发，用递归找到所有的path，将path沿途的所有线段加入到距离矩阵中即可
    def sumOfDistancesInTree(self, N, edges):
        from functools import reduce

        if N == 1:
            return [0]

        dists = [[-1 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dists[i][i] = 0

        # convert to dict
        edge_dict = {}
        for edge in edges:
            edge_dict.setdefault(edge[0], []).append(edge[1])       # collections.defaultdict(list)
            edge_dict.setdefault(edge[1], []).append(edge[0])

            dists[edge[0]][edge[1]] = dists[edge[1]][edge[0]] = 1

        # end_point = -1
        #
        # # first find a end-point
        # for k, v in edge_dict.items():
        #     if len(v) == 1:
        #         end_point = k
        #         break

        # for i in range(N):
        #     count = reduce(lambda x, y: x + 1 if y[0] == i or y[1] == i else x, edges, 0)
        #
        #     if count == 1:
        #         break

        # print(edge_dict)
        # print(end_point)

        # self.sumOfDistancesInTreeR(edge_dict, [end_point], dists)

        in_progress = True
        while in_progress:
            in_progress = False
            is_find = False

            for i in range(N):
                if is_find:
                    break
                for j in range(N):
                    if dists[i][j] < 0:
                        in_progress = True
                        if len(edge_dict[i]) == 1:
                            self.sumOfDistancesInTreeR(edge_dict, [i], dists)
                            is_find = True
                            break
                        elif len(edge_dict[j]) == 1:
                            self.sumOfDistancesInTreeR(edge_dict, [j], dists)
                            is_find = True
                            break

        # if any(dists[i][j] < 0 for i in range(N) for j in range(N)):
        #     print('err')
        #     print(dists)
        #
        #     for i in range(N):
        #         for j in range(N):
        #             if dists[i][j] < 0:
        #                 print('i={}, j={}'.format(i, j))

        sums = [0] * N
        for i in range(N):
            for j in range(N):
                sums[i] += dists[i][j]

        return sums

    def sumOfDistancesInTreeR(self, edge_dict, path, dists):
        cur_node = path[-1]

        except_node = -1
        if len(path) > 1:
            except_node = path[-2]

        # print(path)

        for next_node in edge_dict[cur_node]:
            if next_node != except_node:
                path.append(next_node)

                for i, v in enumerate(path[:-2]):
                    if dists[v][next_node] < 0:
                        dists[v][next_node] = dists[next_node][v] = len(path) - i - 1

                self.sumOfDistancesInTreeR(edge_dict, path, dists)
                path.pop()
