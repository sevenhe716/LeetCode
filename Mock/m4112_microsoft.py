# Time:  O(n)
# Space: O(1)

# Ideas:
# mark


class Solution:
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