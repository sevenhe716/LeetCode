# Time:  O(n)
# Space: O(1)

# 解题思路：
# 优化思路：无需维护subsum，直接sum然后依次减去当前元素即可


class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """

        si = [ord(c) - ord('a') for c in S]

        for i, shift in enumerate(shifts):
            shift %= 26

        shifts2 = [0] * len(shifts)
        shifts2[-1] = shifts[-1]
        for i in range(len(shifts) - 1, 0, -1):
            shifts2[i - 1] = shifts[i - 1] + shifts2[i]
            if shifts2[i - 1] >= 26:
                shifts2[i - 1] = shifts2[i - 1] % 26

        for i, shift in enumerate(shifts2):
            si[i] += shift
            if si[i] >= 26:
                si[i] = si[i] % 26

        return ''.join([chr(num + ord('a')) for num in si])


    # Prefix Sum
    def shiftingLetters1(self, S, shifts):
        sm, res = sum(shift % 26 for shift in shifts) % 26, ""  # sum可以直接模26，负数的模也是[0, n-1]
        for i, s in enumerate(shifts):
            move, sm = ord(S[i]) + sm % 26, sm - s
            res += chr(move > 122 and move - 26 or move)
        return res
