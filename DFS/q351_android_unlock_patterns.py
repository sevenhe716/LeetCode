# Time:  O(n)
# Space: O(1)

# Ideas:
# record all in brute force
# dfs
import itertools
import re
from functools import lru_cache


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        througth_dict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
        self.res = 0

        def dfs(last, used: set, left: set):
            if len(used) > n:
                return
            if m <= len(used) <= n:
                self.res += 1

            for num in left:
                if last:
                    key = (last, num) if last < num else (num, last)
                    if key in througth_dict:
                        if througth_dict[key] in left:
                            continue
                used.add(num)
                left.remove(num)
                dfs(num, used, left)
                left.add(num)
                used.remove(num)

        dfs(None, set(), {i for i in range(1, 10)})
        return self.res


class Solution1:
    def numberOfPatterns1(self, m, n, patterns=[]):
        while len(patterns) <= n:
            # 在13或31之前没有出现过2的字符串模式
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += sum(not bad(''.join(p))
                            for p in itertools.permutations('123456789', len(patterns))),
        return sum(patterns[m:n + 1])


    def numberOfPatterns2(self, m, n, patterns=[['']]):
        while len(patterns) <= n:
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += [p + d for p in patterns[-1] for d in '123456789'
                         if d not in p and not bad(p + d)],
        return sum(map(len, patterns[m:n + 1]))

    # lru_cache
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        unallowed = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: [],
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8}
        }

        @lru_cache(maxsize=None)
        def helper(n, last, visited):
            if n == 0:
                return 1
            s = sum(helper(n - 1, x, visited | (1 << x)) for x in range(1, 10) if
                    not (1 << x) & visited and (not x in unallowed[last] or (1 << unallowed[last][x]) & visited))
            # print(n, last, visited, s)
            return s

        s = sum(helper(i - 1, x, 1 << x) for i in range(m, n + 1) for x in range(1, 10))
        print(helper.cache_info())
        return s