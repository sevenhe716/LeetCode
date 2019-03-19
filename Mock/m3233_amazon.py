# Time:  O(n)
# Space: O(1)

# Ideas:
# product forward and backward


class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        n, product = len(nums), 1
        res = [0] * n
        for i in range(n):
            res[i] = product
            product *= nums[i]

        product = 1
        for i in range(n)[::-1]:
            res[i] *= product
            product *= nums[i]

        return res