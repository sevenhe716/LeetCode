# Time:  O(n)
# Space: O(1)

# Ideas:
# use counter
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = Counter(secret)
        A, B = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
                cnt[s] -= 1

        for s, g in zip(secret, guess):
            if s != g and g in cnt and cnt[g] > 0:
                B += 1
                cnt[g] -= 1

        return '{}A{}B'.format(A, B)