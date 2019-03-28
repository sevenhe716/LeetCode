# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution1:
    # O(nlog(n))的时间复杂度
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from bisect import bisect_left

        nums_sort = sorted([i + i for i in nums])
        count = 0

        for i in range(len(nums)):
            pos = bisect_left(nums_sort, nums[i] + nums[i])
            nums_sort = nums_sort[:pos] + nums_sort[pos+1:]
            count += bisect_left(nums_sort, nums[i])

        return count


class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)


    def insert_value(self, index):
        index += 1

        while index > 0:
            self.tree[index] += 1
            index -= index & (-index)


    def get_sum(self, index):
        result, index = 0, index + 1

        while index <= self.size:
            result += self.tree[index]
            index += index & (-index)
        return result


class Solution3(object):
    def reversePairs(self, nums):
        import bisect
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        result = 0
        bit_tree = BIT(len(nums))
        for number in nums:
            result += bit_tree.get_sum(bisect.bisect_left(sorted_nums, number * 2 + 1))
            bit_tree.insert_value(bisect.bisect_left(sorted_nums, number))
        return result