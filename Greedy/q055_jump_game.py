# Time:  O(n)
# Space: O(1)

# 解题思路：
# 观察规律可以得出，如果无法抵达终点，在路径中必定存在至少一个0，并且这个0之前至少存在第n个元素的小于等于n
# 遍历顺序应该是从后往前，因为当后面的0已经发现不满足条件时，无需回头重新找下一个0，而是基于当前索引位置继续往前找
# 因为不满足条件的点也必定会jump这些0，one-pass即可
# 特殊情况：当0为最后一个时，无需跳过


class Solution:
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = len(nums) - 1

        if nums == [0]:
            return True

        while index >= 0:
            while index >= 0 and nums[index] != 0:
                index -= 1

            if index < 0:
                return True

            if index == len(nums) - 1:
                last = True
            else:
                last = False

            offset = 1
            if last:
                while index - offset >= 0 and nums[index - offset] < offset:
                    offset += 1
            else:
                while index - offset >= 0 and nums[index - offset] <= offset:
                    offset += 1

            if index - offset < 0:
                return False

            index -= offset

        return True

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = len(nums) - 2

        while index >= 0:
            while index >= 0 and nums[index] != 0:
                index -= 1

            if index < 0:
                return True

            offset = 1
            while index - offset >= 0 and nums[index - offset] <= offset:
                offset += 1

            if index - offset < 0:
                return False

            index -= offset

        return True


class SolutionF:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        can = True
        smallest_idx = n - 1

        for i in range(n - 2, -1, -1):
            can = i + nums[i] >= smallest_idx
            if can:
                smallest_idx = i
        return can


class SolutionF2:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
