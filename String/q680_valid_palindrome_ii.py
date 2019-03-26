# Time:  O(n)
# Space: O(1)

# Ideas:
# two-pointer?


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def valid(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            # return s[left:right+1] == s[left:right+1][::-1]

        while left <= right:
            if s[left] != s[right]:
                if valid(left + 1, right) or valid(left, right - 1):
                    return True
                else:
                    return False
            left += 1
            right -= 1

        return True


class Solution1:
    def validPalindrome1(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
        return True

    # 最快的方法还是字符串拼接
    def validPalindrome2(self, s: 'str') -> 'bool':
        sReversed = s[::-1]
        if s == sReversed:
            return True
        for i in range(len(s)):
            if s[i] != sReversed[i]:
                if i == len(s) - 1:
                    return True
                return s[i + 1:] == sReversed[i:len(s) - 1 - i] + sReversed[len(s) - i:] or \
                       s[i:len(s) - 1 - i] + s[len(s) - i:] == sReversed[i + 1:]
