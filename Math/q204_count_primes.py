# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        if n < 3:
            return 0
        isPrimes = [True] * n
        isPrimes[0] = isPrimes[1] = False
        for i in range(2, int(n ** 0.5)+1):
            if isPrimes[i]:
                isPrimes[i*i::i] = [False] * len(isPrimes[i*i::i])  # i*k(k<i)已经被标记过了
        return sum(isPrimes)