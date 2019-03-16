# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-', '')
        n = len(S)
        if n <= K:
            return S
        first = n % K
        res = ''
        if first > 0:
            res += S[:first] + '-'
        res += '-'.join(S[i:i + K] for i in range(first, n, K))
        return res
