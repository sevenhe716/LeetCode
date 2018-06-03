# Time:  O(n)
# Space: O(1)

# 解题思路：
# 1-pass O(1) space


class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, 0
        longest = 0
        count = 0
        up = False
        down = False

        for i in range(len(A)-1):
            if down:
                if A[i] > A[i + 1]:
                    count += 1
                else:
                    right = i
                    longest = max(longest, right - left + 1)
                    count = 0
                    down = False
                    if A[i] < A[i + 1]:
                        left = i
                        up = True
                    else:
                        up = False
            elif up:
                if A[i] < A[i + 1]:
                    count += 1
                elif A[i] > A[i + 1]:
                    count += 1
                    down = True
                else:
                    up = False
                    down = False
                    count = 0
            else:
                if A[i] < A[i + 1]:
                    up = True
                    left = i
                    count += 1

        if up and down:
            right = len(A) - 1
            longest = max(longest, right - left + 1)

        return longest


# 写法更简洁，但是效率上是有损失的
class Solution1:
    # 思路类似，但是更简洁，主要优化在无需判断当前处于哪个阶段
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]       # 直接加，无需判断处于哪个阶段
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)       # 这里会导致比较次数变多
        return res

    # two-pass
    def longestMountain1(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])