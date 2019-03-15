# Time:  O(n)
# Space: O(1)

# 解题思路：
# 不用除法，且是常数空间复杂度，线性时间复杂度
# 利用存储结果的空间，两个方向累乘，就可以在乘积中去掉当前的值


class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        n = len(nums)
        res, product = [0] * n, 1
        for i in range(n):
            res[i] = product
            product *= nums[i]
        product = 1
        for i in range(n)[::-1]:
            res[i] *= product
            product *= nums[i]
        return res