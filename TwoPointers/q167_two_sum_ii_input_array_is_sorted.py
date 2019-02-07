# Time:  O(n)
# Space: O(1)

# 解题思路：
# 有序数组二数之和，二分查找时间复杂度为nlog(n)，固定一个数，用差值查找另一个数
# 双指针法，时间复杂度为n


class Solution:
    # binary search
    def twoSum1(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        # 无法直接用二分查找来同时卡上下界
        # left, right = 0, len(numbers)-1
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if numbers[left] + numbers[right] == target:
        #         return [left+1, right+1]
        #     elif numbers[left] + numbers[right] < target:
        #         left = mid
        #     else:
        #         right = mid
        #
        # return [0, 0]
        for i in range(len(numbers) - 1):
            start = i + 1
            end = len(numbers) - 1
            new_target = target - numbers[i]
            while start <= end:
                mid = (start + end) // 2
                if new_target == numbers[mid]:
                    return [i + 1, mid + 1]
                elif new_target > numbers[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return None

    # two pointers
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [0, 0]