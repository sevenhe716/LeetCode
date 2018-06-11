# Time:  O(n)
# Space: O(1)

# 解题思路：
# 注意k是从1开始的，转换为n!，通过取模的方式，得出当前是剩余排序数组中的第几个数


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        k -= 1
        nums = list(range(1, n+1))
        num = 0

        factor = 1
        for i in range(1, n):
            factor *= i

        for i in range(n-1, 0, -1):
            index, k = divmod(k, factor)
            factor //= i

            num += nums[index]
            num *= 10
            nums = nums[:index] + nums[index+1:]

        num += nums[0]
        return str(num)

