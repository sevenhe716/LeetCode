# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 二分查找的思路更好


class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil

        aver = ceil(sum(piles) / H)

        for i in range(aver, sum(piles)):
            total = 0
            for p in piles:
                total += ceil(p / i)
            if total <= H:
                return i

        return 0

class Solution1:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def enough(speed,H,piles):
            time=0
            for num in piles:
                if num%speed:
                    time+=num//speed+1
                else:
                    time+=num//speed
            return time<=H
        lo=1
        hi=max(piles)
        while hi>lo:
            m=(lo+hi)//2
            if not enough(m,H,piles):
                lo=m+1
            else:
                hi=m
        return lo