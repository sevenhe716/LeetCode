# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    # greedy
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        a_s, l_s = 0, 0

        print()

        while True:
            if len(piles) == 2:
                a_s += max(piles)
                l_s += min(piles)
                return a_s > l_s
            else:
                if piles[0] - max(piles[1], piles[-1]) >= piles[-1] - max(piles[0], piles[-2]):
                    a_s += piles[0]
                    print(piles[0])
                    piles = piles[1:]
                else:
                    a_s += piles[-1]
                    print(piles[-1])
                    piles = piles[:len(piles) - 1]

                if piles[0] - max(piles[1], piles[-1]) >= piles[-1] - max(piles[0], piles[-2]):
                    l_s += piles[0]
                    print(piles[0])
                    piles = piles[1:]
                else:
                    l_s += piles[-1]
                    print(piles[-1])
                    piles = piles[:len(piles) - 1]
                #
                # if piles[0] == piles[-1]:
                #     if piles[1] >= piles[-2]:
                #         a_s += piles[-1]
                #         print(piles[-1])
                #         piles = piles[:len(piles) - 1]
                #     else:
                #         a_s += piles[0]
                #         print(piles[-1])
                #         piles = piles[1:]
                # elif piles[0] > piles[-1]:
                # # if max(piles[0], piles[1], piles[-1]) >= max(piles[0], piles[-2], piles[-1]):
                #     a_s += piles[0]
                #     print(piles[0])
                #     piles = piles[1:]
                # else:
                #     a_s += piles[-1]
                #     print(piles[-1])
                #     piles = piles[:len(piles)-1]
                #
                # if piles[0] == piles[-1]:
                #     if piles[1] >= piles[-2]:
                #         l_s += piles[-1]
                #         print(piles[-1])
                #         piles = piles[:len(piles) - 1]
                #     else:
                #         l_s += piles[0]
                #         print(piles[-1])
                #         piles = piles[1:]
                # elif piles[0] > piles[-1]:
                # # if max(piles[0], piles[1], piles[-1]) >= max(piles[0], piles[-2], piles[-1]):
                #     l_s += piles[0]
                #     print(piles[0])
                #     piles = piles[1:]
                # else:
                #     l_s += piles[-1]
                #     print(piles[-1])
                #     piles = piles[:len(piles)-1]
                #
