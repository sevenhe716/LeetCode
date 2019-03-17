# Time:  O(n)
# Space: O(1)

# Ideas:
# reverse every words, can use point or lib
from functools import reduce


class Solution:
    def reverseWords1(self, s: str) -> str:
        return reduce(lambda x, y: x + ' ' + y[::-1], s.split(' '), '')[1:]

    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1], s.split(' ')))
