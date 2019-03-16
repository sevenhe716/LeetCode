# Time:  O(n)
# Space: O(1)

# 解题思路：
# 加法模拟器


class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = sorted(list(set(time[:2] + time[3:])))
        t = list(time[:2] + time[3:])

        def valid(t):
            return ''.join(t[:2]) < '24' and ''.join(t[2:]) < '60'

        carry = True
        for i in range(4)[::-1]:
            if not carry:
                break
            while True:
                carry = False
                next_idx = nums.index(t[i]) + 1
                if next_idx == len(nums):
                    carry = True
                    next_idx = 0
                t[i] = nums[next_idx]
                if valid(t):
                    break

        return ''.join(t[:2]) + ':' + ''.join(t[2:])