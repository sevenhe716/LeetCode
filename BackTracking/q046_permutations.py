# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 常规思路就是用set，遍历所有元素然后递归生成下一个，这里需要注意的是，set在每层遍历时需要拷贝一份，这是很大的开销


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        num_set = set(nums)
        permutations = []

        def permuteR(permutation):
            if not num_set:
                return

            num_copy = set(num_set)

            for num in num_copy:
                if len(num_set) == 1:
                    permutations.append(permutation + [num])
                    return

                num_set.remove(num)
                permutation.append(num)
                permuteR(permutation)
                num_set.add(num)
                permutation.remove(num)

        permuteR([])
        return permutations


# Intuition:
#
# Start with the first element of the array as the root node
# Place second element at all possible places i.e at front and behind of the first number to create two permutations of both of these numbers.
# Now the third number can be placed at 3 positions in each of the previous two nodes.
# Similar method for the next numbers of the array. To keep track of the next numbers, I am using the index variable.
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        stack = [[[nums[0]], 0]]
        i = 0
        res = []

        while stack:
            arr, index = stack.pop()
            if index == len(nums) - 1:
                res.append(arr)
            else:
                for i in range(len(arr) + 1):
                    newPermutation = arr[:i] + [nums[index + 1]] + arr[i:]
                    stack.append([newPermutation, index + 1])

        return res


# 原地
class Solution3:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        res = [nums[:]]
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                j = n - 1
                while nums[j] < nums[i - 1]:
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                res.append(nums[:])
                i = n - 1
            else:
                i -= 1

        return res
