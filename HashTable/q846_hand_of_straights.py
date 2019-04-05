# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# counter计数器加索引排序
import collections


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """

        # fast verify
        if len(hand) % W:
            return False

        count = len(hand) // W

        counter = collections.Counter(hand)
        sort_key = sorted(counter.keys())

        min_i = 0

        for _ in range(count):
            key = sort_key[min_i]
            while counter[key] <= 0:
                min_i += 1
                if min_i >= len(sort_key):
                    return False
                key = sort_key[min_i]

            for _ in range(W):
                if key not in counter or counter[key] <= 0:
                    return False
                else:
                    counter[key] -= 1

                key += 1

        return True


# 思路类似，使用最小堆，而非sorted list
class Solution1:
    def isNStraightHand(self, hand, W):

        from collections import defaultdict
        from heapq import heappop, heapify

        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l % W:
            return False
        if W == 1:
            return True

        # first we count the numbers
        cnt = defaultdict(int)
        for i in hand:
            cnt[i] += 1
        # then we build the minimum heap
        heapify(hand)

        for i in range(l // W):
            # first we find the starting number of current group
            start = heappop(hand)
            while cnt[hand] == 0:  # if the number is no loner available
                start = heappop(hand)  # we pop again

            # Now we find the all other numbers in the group
            for i in range(W):
                cnt[start] -= 1  # decrease its counts
                if cnt[start] < 0:  # the number is not available
                    return False
                start += 1
        return True


class SolutionL:
    # 效率低，但是有点意思
    def isNStraightHand(self, hand, W):
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base + i)
            except:
                return False
        return True

    # O(MlogM + MW)
    def isNStraightHand2(self, hand, W):
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(W)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

    # deque O(MlogM)
    def isNStraightHand3(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0