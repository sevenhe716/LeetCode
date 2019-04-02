# Time:  O(n)
# Space: O(1)

# Ideas:
# record all in brute force
# dfs


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        through_dict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
        self.res = 0

        def dfs(last, used: set, left: set):
            if len(used) > n:
                return
            if m <= len(used) <= n:
                self.res += 1

            for num in left:
                if last:
                    key = (last, num) if last < num else (num, last)
                    if key in through_dict:
                        if through_dict[key] in left:
                            continue
                used.add(num)
                left.remove(num)
                dfs(num, used, left)
                left.add(num)
                used.remove(num)

        dfs(None, set(), {i for i in range(1, 10)})
        return self.res
