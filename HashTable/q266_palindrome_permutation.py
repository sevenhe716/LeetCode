# Time:  O(n)
# Space: O(1)

# 解题思路：
# 任意排列满足回文的充要条件就是除一个字符以外所有字符的个数为偶数
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        first = True

        # 提前终止循环，执行效率更高
        for count in cnt.values():
            if count % 2:
                if first:
                    first = False
                else:
                    return False
        return True


# one-line pythonic
class Solution1:
    def canPermutePalindrome1(self, s: str) -> bool:
        return len([count for count in Counter(s).values() if count % 2 == 1]) <= 1

    def canPermutePalindrome(self, s: str) -> bool:
        return len(list(filter(lambda x: x % 2, Counter(s).values()))) <= 1

    def canPermutePalindrome3(self, s: str) -> bool:
        return sum(1 for _ in filter(lambda x: x % 2, Counter(s).values())) <= 1

    def canPermutePalindrome4(self, s: str) -> bool:
        return sum(v % 2 for v in Counter(s).values()) < 2
