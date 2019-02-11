# Time:  O(nlogn)
# Space: O(1)

# 解题思路：
# 1. 二分法，至少有一边是多数元素
# 2. 每次去掉两个不同的元素，最终剩下的一种就是主元素
# 3. 排序，排完序之后中位数必定是主元素
# 4. HashMap统计元素个数
import collections

class Solution:
    # 排序
    def majorityElement1(self, nums: 'List[int]') -> 'int':
        return sorted(nums)[(len(nums)-1) // 2]

    # 去掉两个不同的元素，即统计某个元素的个数
    def majorityElement2(self, nums: 'List[int]') -> 'int':
        # count = 0
        # candidate = None
        #
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)

        cur_num, count = None, 0
        for num in nums:
            if cur_num != num:
                if count > 0:
                    count -= 1
                else:
                    cur_num = num
                    count = 1
            else:
                count += 1

        return cur_num

    # HashMap
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution1:
    # 分治法，如果两边结果不统一，则计数统计
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)


class Solution2:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        size = len(nums)
        mask = 1
        ret = 0
        for i in range(32):
            count = 0
            for j in range(size):
                if mask & nums[j]:
                    count += 1
                if count > size // 2:
                    ret |= mask
                mask <<= 1
        return ret

class Solution3:
    # Bit manipulation
    def majorityElement(self, nums):
        bit = [0]*32
        for num in nums:
            for j in range(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums)//2:
                # if the 31th bit if 1,
                # it means it's a negative number
                if i == 31:
                    res = -((1<<31)-res)
                else:
                    res |= 1 << i
        return res
