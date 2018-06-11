# Time:  O(n)
# Space: O(1)

# 解题思路：
# 求subsum之和，为负后清零


class Solution:
    # subsum
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        total = 0

        for i in nums:
            total += i
            largest = max(largest, total)
            if total < 0:
                total = 0

        return largest


# divide and conquer
class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(nums):  # return [leftmax,rightmax,allmax,total]
            if not nums:
                return [float("-inf"), float("-inf"), float("-inf"), 0]
            d = nums[len(nums) // 2]
            left = helper(nums[:len(nums) // 2])
            right = helper(nums[len(nums) // 2 + 1:])
            ans = [0, 0, 0, 0]
            ans[3] = left[3] + right[3] + d
            ans[0] = max(left[0], left[3] + d + right[0], left[3] + d)
            ans[1] = max(right[1], right[3] + d, right[3] + d + left[1])
            ans[2] = max(left[2], right[2], d, d + left[1], d + right[0], d + left[1] + right[0])
            return ans

        return helper(nums)[2]


# dp
# maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element.
# maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];
class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        largest = dp[0] = nums[0]

        for i in range(n):
            dp[i] = nums[i] + (dp[i - 1] if dp[i-1] > 0 else 0)
            largest = max(largest, dp[i])

        return largest


# 跟我的思路实际上是一致的
class SolutionF:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        last_max = nums[0]

        for i in range(1, len(nums)):
            last_max = max(last_max + nums[i], nums[i])
            result = max(last_max, result)

        return result
