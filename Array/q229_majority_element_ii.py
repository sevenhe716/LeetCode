# Time:  O(n)
# Space: O(1)

# Ideas:
# mark
import collections


class Solution:
    # Boyer-Moore Majority Vote algorithm generalization
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        c1, c2 = nums[0], nums[0]
        s1, s2 = 0, 0
        for n in nums:
            if c1 == n:
                s1 += 1
            elif c2 == n:
                s2 += 1
            else:
                if s1 == 0:
                    c1, s1 = n, 1
                elif s2 == 0:
                    c2, s2 = n, 1
                else:
                    s1 -= 1
                    s2 -= 1

        s1, s2 = 0, 0
        for n in nums:
            if c1 == n:
                s1 += 1
            elif c2 == n:
                s2 += 1

        res = []
        if s1 > len(nums) // 3:
            res.append(c1)
        if s2 > len(nums) // 3:
            res.append(c2)
        return res


class Solution1:
    def majorityElement(self, nums):
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                # 使用到counter-的运算符重载，很精髓
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums) // 3]

    def majorityElement1(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]