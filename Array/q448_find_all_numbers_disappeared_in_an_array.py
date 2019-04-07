# Time:  O(n)
# Space: O(1)

# 解题思路：
# 要求不用额外的空间，而且O(n)的时间复杂度
# 难点在于不使用额外的空间，因此突破口就是利用原数组O(n)的空间
# 因此可以将1-n的数值减1作为索引的下标


class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


# 交换元素，每次交换至少保证一个元素的位置正确，因此时间复杂度为O(n)
# 当前元素不在正确的位置，且想要的交换的元素与其不相等
class Solution1:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                # python的坑：这种情况下批量赋值不是同时执行的，nums[nums[i] - 1]会在nums[i]赋值之后执行
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]
