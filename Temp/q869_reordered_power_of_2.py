# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        biggest = 10 ** 9
        cur = 1
        n = 0

        power2 = ['1']
        while cur < biggest:
            n += 1
            cur = 2 ** n
            power2.append(''.join(sorted(str(cur))))


        return ''.join(sorted(str(N))) in power2


