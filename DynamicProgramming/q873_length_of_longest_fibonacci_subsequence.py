# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        max_len = 0
        A_set = set(A)

        def backtrack(cur_seq):
            nonlocal max_len
            next = cur_seq[-1] + cur_seq[-2]
            if next in A_set:
                cur_seq.append(next)
                backtrack(cur_seq)
            else:
                max_len = max(max_len, len(cur_seq))

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                cur_seq = [A[i], A[j]]
                backtrack(cur_seq)

        if max_len >= 3:
            return max_len
        else:
            return 0


    def lenLongestFibSubseq2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        dp = [{} for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                tmp = A[i] - A[j]
                if tmp in dp[j]:
                    dp[i][A[j]] = dp[j][tmp] + 1
                    ans = max(ans, dp[i][A[j]])
                else:
                    dp[i][A[j]] = 2
        return ans

