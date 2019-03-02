# Time:  O(n)
# Space: O(1)

# 解题思路：
# 按低到高位依次变换，用异或位运算，有个隐藏条件是，数字不能重复
# 寻找规律，依次异或：
# 0 0 1
# 0 1 0
# 0 0 1
# 1 0 0
# 0 0 1
# 0 1 0
# 0 0 1
# 即从1开始的自然数，取最低位的1，X & -X得到最低位的1

# yet another elegant, fast and easy-understand Python solution(4 lines)
# bit-manipulation


class Solution:
    def grayCode(self, n: int) -> 'List[int]':
        res = [0]
        for i in range(1, 2**n):
            res.append(res[-1] ^ (i & -i))
        return res
