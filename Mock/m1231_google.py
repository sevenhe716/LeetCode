# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        digits_map = {i: i + 1 for i in range(10)}
        digits_map[9] = 0

        carry = True
        for i in range(len(digits))[::-1]:
            if not carry:
                break
            carry = False
            digits[i] = digits_map[digits[i]]
            if digits[i] == 0:
                carry = True
        if carry:
            digits.insert(0, 1)

        return digits
