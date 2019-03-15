# Time:  O(n)
# Space: O(1)

# 解题思路：
# 移除dash，并且每K个一组，特殊处理头节点
# 另一个思路是边遍历边构造


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr = list(S.replace('-', '').upper())
        n = len(arr)
        if n <= K:
            return ''.join(arr)
        first, res = n % K, ''
        if first > 0:
            res += ''.join(arr[:first]) + '-'
        return res + '-'.join(''.join(arr[i:i+K]) for i in range(first, n, K))


class Solution1:
    # 反序可以统一和简化逻辑
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        mod_s = S.replace("-", "").upper()[::-1]
        return "-".join([mod_s[i: i + K] for i in range(0, len(mod_s), K)])[::-1]