# Time:  O(n)
# Space: O(1)

# 解题思路：
# 优化思路，先构造一个索引集合，再统一进行替换


class Solution:
    # 优化：in string比in array快很多
    # 减少分支判断
    def reverseVowels1(self, s: 'str') -> 'str':
        res = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s)-1
        while left < right:
            while res[left] not in vowels:
                left += 1
                if left >= right:
                    return ''.join(res)
            while res[right] not in vowels:
                right -= 1
                if left >= right:
                    return ''.join(res)
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return ''.join(res)

    def reverseVowels(self, s: 'str') -> 'str':
        res = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and res[left] not in 'aeiouAEIOU':
                left += 1
            while left < right and res[right] not in 'aeiouAEIOU':
                right -= 1
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return ''.join(res)

    def reverseVowels2(self, s: 'str') -> 'str':
        res = list(s)
        vowels_index = [i for i, c in enumerate(s) if c in 'aeiouAEIOU']
        for i in range(len(vowels_index) // 2):
            res[vowels_index[i]], res[vowels_index[~i]] = res[vowels_index[~i]], res[vowels_index[i]]
        return ''.join(res)

    def reverseVowels(self, s: 'str') -> 'str':
        res = list(s)
        vowels_index = [i for i, c in enumerate(s) if c in 'aeiouAEIOU']
        half = len(vowels_index) // 2
        for i, j in zip(vowels_index[:half], vowels_index[-1:-half-1:-1]):
            res[i], res[j] = res[j], res[i]
        return ''.join(res)