# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 延续三数之和的思路，固定第一个数，用两个指针从两端往中间找两数之和，与最小值比较


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        max_sum = sum(nums[-3:])
        min_sum = sum(nums[:3])

        if max_sum <= target:
            return max_sum

        if min_sum >= target:  # 处理特殊情况，在某些小的数组中，可以更快的得出结果
            return min_sum

        closest = 2147483647

        for index, i in enumerate(nums):
            target2 = target - i
            l, r = index + 1, len(nums) - 1

            while l < r:
                diff = target2 - nums[l] - nums[r]
                if diff == 0:
                    return target
                elif diff > 0:
                    l += 1
                else:
                    r -= 1

                if abs(diff) < abs(closest):
                    closest = diff

        return target - closest


class Solution1(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return result


# 整体思路相同，只是有些特殊处理，如maxSum minSum，导致在特定的测试用例上快很多
class SolutionF(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) <= 3:
            return sum(nums)

        nums.sort()
        maxSum = sum(nums[-3:])
        minSum = sum(nums[:3])

        if target <= minSum:
            return minSum
        if target >= maxSum:
            return maxSum

        if target - minSum > maxSum - target:
            closet = maxSum
            distance = maxSum - target
        else:
            closet = minSum
            distance = target - minSum

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < distance:
                    closet = s
                    distance = abs(s - target)

                if s == target:
                    return closet

                elif s > target:
                    if nums[i] + 2 * nums[left] > target:
                        break

                    right -= 1

                else:
                    if nums[i] + 2 * nums[right] < target:
                        break

                    left += 1

        return closet

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size < 3:
            return 0
        nums.sort()
        i = 0  # fix the first index
        ans = nums[0] + nums[1] + nums[size - 1]  # ans is used to record the solution
        while i < size - 2:
            tmp = target - nums[i]
            j = i + 1
            k = size - 1
            while j < k:
                if nums[j] + nums[k] == tmp:
                    return target
                if nums[j] + nums[k] > tmp:
                    if nums[j] + nums[j + 1] >= tmp:
                        if nums[j] + nums[j + 1] - tmp < abs(ans - target):  # 提前终止循环，优化的关键
                            ans = nums[i] + nums[j] + nums[j + 1]
                        break
                    tmpans = nums[i] + nums[j] + nums[k]
                    if tmpans - target < abs(ans - target):
                        ans = tmpans
                    k -= 1
                else:
                    if nums[k] + nums[k - 1] <= tmp:
                        if tmp - nums[k] - nums[k - 1] < abs(ans - target):  # 提前终止循环，优化的关键
                            ans = nums[i] + nums[k - 1] + nums[k]
                        break
                    tmpans = nums[i] + nums[j] + nums[k]
                    if target - tmpans < abs(ans - target):
                        ans = tmpans
                    j += 1
            i += 1
            if ans == target:
                return target
        return ans
