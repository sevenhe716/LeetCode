# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        n = R * C
        ans = []
        l = 2
        dir = 0

        steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        cur = [r0, c0]
        ans.append(cur.copy())

        while len(ans) < n:
            for _ in range(l // 2):
                # right down left up
                cur[0] += steps[dir][0]
                cur[1] += steps[dir][1]

                if 0 <= cur[0] < R and 0 <= cur[1] < C:
                    ans.append(cur.copy())
                    if len(ans) >= n:
                        break

            l += 1
            dir += 1
            dir %= 4
            # print(dir)


        return ans