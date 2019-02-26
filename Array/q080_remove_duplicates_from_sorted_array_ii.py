# Time:  O(n)
# Space: O(1)

# 解题思路：
# 记录当前偏移量，并往前赋值即可


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        # 记录当前偏移量，并往前赋值即可
        last, first, offset = None, True, 0
        for i, num in enumerate(nums):
            if num != last:
                last, first = num, True
            else:
                if first:
                    first = False
                else:
                    offset += 1
            nums[i - offset] = num

        return len(nums) - offset
