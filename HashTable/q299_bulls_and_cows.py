# Time:  O(n)
# Space: O(1)

# Ideas:
# use counter
from collections import Counter
from collections import defaultdict
import operator


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 遍历了三次
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


class Solution1:
    def getHint1(self, secret: str, guess: str) -> str:
        bulls = 0
        sec = defaultdict(int)
        gue = defaultdict(int)
        # O(n)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sec[s] += 1
                gue[g] += 1
        cows = 0
        # O(K)
        for g, count in gue.items():
            if g in sec:
                cows += min(count, sec[g])
        return str(bulls) + 'A' + str(cows) + 'B'

    # 简洁优美
    def getHint2(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, both - bulls)

    # 更漂亮的写法，& in counter
    def getHint3(self, secret, guess):
        A = sum(a == b for a, b in zip(secret, guess))
        B = Counter(secret) & Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)

    # One Pass solution
    def getHint4(self, secret, guess):
        # use arr instead of dict, but slow than it
        counter = [0] * 10
        bulls, cows = 0, 0
        for i, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                bulls += 1
            else:
                s_i, g_i = ord(s) - ord('0'), ord(g) - ord('0')
                if counter[s_i] < 0: cows += 1
                if counter[g_i] > 0: cows += 1
                counter[s_i] += 1
                counter[g_i] -= 1

        return f'{bulls}A{cows}B'
