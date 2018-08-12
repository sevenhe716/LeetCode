# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections

        a, b = A.split(' '), B.split(' ')
        counter = collections.Counter(a + b)
        return [k for k, v in counter.items() if v == 1]
