# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0

        num = bin(N)[2:]
        in_one = False

        lefts = []
        rights = []

        for i, n in enumerate(num):
            if n == '1':
                if not in_one:
                    lefts.append(i)
                    in_one = True

            else:
                if in_one:
                    rights.append(i-1)
                    in_one = False

        if in_one:
            rights.append(len(num)-1)

        if len(lefts) == 1:
            if lefts[0] == rights[0]:
                return 0
            else:
                return 1

        max_gap = 0
        for i in range(len(lefts) - 1):
            max_gap = max(max_gap, lefts[i + 1] - rights[i])

        print()
        print(N)
        print(lefts, rights)

        return max_gap

