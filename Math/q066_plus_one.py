# Time:  O(n)
# Space: O(1)

# 解题思路：
# 实际上就是实现非负数的加法进位


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry:
            carry = 0
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            i -= 1

        if carry:
            # digits = [1] + digits
            digits.insert(0, 1)

        return digits
