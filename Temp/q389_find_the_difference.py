# Time:  O(n)
# Space: O(1)

# 解题思路：
# 两字符串求和的差值
from functools import reduce

# dict缓存
letter_map = {chr(i + ord('a')): i for i in range(26)}


class Solution:
    def findTheDifference(self, s: 'str', t: 'str') -> 'str':
        return chr(reduce(lambda x, y: x + letter_map[y], t, 0) -
                   reduce(lambda x, y: x + letter_map[y], s, 0) + ord('a'))
