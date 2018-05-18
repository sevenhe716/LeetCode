
class Solution1:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        str_list = []

        if not num:
            return '0'

        neg = True if num < 0 else False
        num = abs(num)

        while num != 0:
            num, remain = divmod(num, 7)
            str_list.insert(0, str(remain))

        if neg:
            return '-' + ''.join(str_list)
        else:
            return ''.join(str_list)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution2:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_values = []
        self.findBottomLeftValueR(root, 1, left_values)

        return left_values[-1]

    def findBottomLeftValueR(self, root, depth, left_values):
        if len(left_values) == depth - 1:
            left_values.append(root.val)

        if root.left:
            self.findBottomLeftValueR(root.left, depth + 1, left_values)

        if root.right:
            self.findBottomLeftValueR(root.right, depth + 1, left_values)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution3:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        max_values = []
        self.largestValuesR(root, 1, max_values)

        return max_values

    def largestValuesR(self, root, depth, max_values):
        if len(max_values) == depth - 1:
            max_values.append(root.val)
        else:
            if root.val > max_values[depth - 1]:
                max_values[depth - 1] = root.val

        if root.left:
            self.largestValuesR(root.left, depth + 1, max_values)

        if root.right:
            self.largestValuesR(root.right, depth + 1, max_values)



class Solution:
    # O(n^2)的时间复杂度
    def reversePairs1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from bisect import bisect_left
        nums_sort = sorted([i + i for i in nums])

        count = 0
        for i in range(len(nums)):
            pos = bisect_left(nums_sort, nums[i] + nums[i])
            nums_sort = nums_sort[:pos] + nums_sort[pos + 1:]
            count += bisect_left(nums_sort, nums[i])

        return count

    # O(nlog(n))的时间复杂度
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from bisect import bisect_left

        nums_sort = sorted([i + i for i in nums])

        # two_sums = [i + i for i in nums]

        count = 0

        for i in range(len(nums)):
            pos = bisect_left(nums_sort, nums[i] + nums[i])
            nums_sort = nums_sort[:pos] + nums_sort[pos+1:]
            count += bisect_left(nums_sort, nums[i])

        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > two_sums[j]:
        #             count += 1

        return count
