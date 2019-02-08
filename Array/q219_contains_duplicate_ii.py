# Time:  O(n)
# Space: O(1)

# 解题思路：
# 第一反应是利用滑动窗口，同样用集合来判重


class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        # 先进行一次预检测，提高效率
        if len(set(nums)) == len(nums):
            return False
        k += 1
        if k > len(nums):       # 防止越界
            k = len(nums)
        slide_window = set(nums[:k])
        if len(slide_window) != k:
            return True
        for i in range(len(nums)-k):
            slide_window.remove(nums[i])
            slide_window.add(nums[i+k])
            if len(slide_window) != k:
                return True
        return False


# 用dict value存储最后一个数字的索引，不错的思路，同时先作预判断提高性能
class Solution1:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        if len(nums) == len(set(nums)):
            return False
        else:
            values = {}
            for pos, val in enumerate(nums):
                if (val in values) and (pos - values[val] <= k):
                    return True
                else:
                    values[val] = pos
            return False

    # 不明白为什么这种解法更快，比前一种解法有以下不足：
    # 1.当检测到反例并没有立刻中断循环返回
    # 2.存储所有索引，空间复杂度更高
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == []: return False
        if len(nums) == len(set(nums)): return False
        num_dict = {i: [] for i in nums}
        min_dist = len(nums)
        for i in range(0, len(nums)):
            key = nums[i]
            num_dict[key].append(i)
            if len(num_dict[key]) > 1:
                min_dist = min(min_dist, (num_dict[key])[-1] - num_dict[key][-2])
        return min_dist <= k