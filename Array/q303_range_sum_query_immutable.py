# Time:  O(n)
# Space: O(1)

# 解题思路：
# 设计一个数据结构，提高区间和的运算效率
# 数组元素不可变，可以缓存子数组和，然后相减即可


class NumArray1:
    # 优化思路：多记录一次元素为0的情况
    def __init__(self, nums: 'List[int]'):
        if nums:
            self.sub_sum = [0] * len(nums)
            self.sub_sum[0] = nums[0]
            for i in range(1, len(nums)):
                self.sub_sum[i] = self.sub_sum[i-1] + nums[i]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.sub_sum[j] - self.sub_sum[i-1] if i > 0 else self.sub_sum[j]


class NumArray:
    # 优化思路：多记录一次元素为0的情况，代码更简洁，分支情况更少
    def __init__(self, nums: 'List[int]'):
        self.sub_sum = [0]
        for num in nums:
            self.sub_sum.append(self.sub_sum[-1] + num)

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.sub_sum[j+1] - self.sub_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)