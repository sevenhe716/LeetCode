# Time:  O(n)
# Space: O(1)

# 解题思路：
# 考虑用回溯，每一步有三种操作方式，add delete或replace
# 优化思路：当步骤已经超过当前最小步骤时，可以提前终止
# 特殊情况，如果一端已经到末尾，则只能添加或删除，步骤直接加差值
# 缓存之前遍历过的结果


class Solution:
    # backtracking
    def minDistance(self, word1, word2):
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
