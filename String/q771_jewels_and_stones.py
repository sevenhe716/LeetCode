# Time:  O(n)
# Space: O(1)

# 解题思路：
#
from collections import Counter
from functools import reduce


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_cnt = Counter(S)
        return reduce(lambda x, y: x + (stone_cnt[y] if y in stone_cnt else 0), J, 0)
        # return reduce(lambda x, y: x + stone_cnt[y], filter(lambda x: x in stone_cnt, J), 0)


# 利用set的O(1)查询时间
class Solution(object):
    def numJewelsInStones1(self, J, S):
        return sum(s in J for s in S)

    def numJewelsInStones2(self, J, S):
        return sum(map(J.count, S))

    def numJewelsInStones3(self, J, S):
        return sum(map(S.count, J))

    def numJewelsInStones4(self, J, S):
        return sum(s in J for s in S)

# 把J转化为regexp
# public int numJewelsInStones(String J, String S) {
#     return S.replaceAll("[^" + J + "]", "").length();
# }