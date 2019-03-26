# Time:  O(n^2)
# Space: O(1)

# Ideas:
# circular array


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if not A:
            return True
        n = len(A)
        for i in range(n):
            if all(A[(i + j) % n] == B[j] for j in range(n)):
                return True
        return False


class Solution1:
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A + A

    # rolling hashing
    def rotateString(self, A, B):
        MOD = 10 ** 9 + 7
        P = 113
        Pinv = pow(P, MOD - 2, MOD)

        hb = 0
        power = 1
        for x in B:
            code = ord(x) - 96
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in A:
            code = ord(x) - 96
            ha = (ha + power * code) % MOD
            power = power * P % MOD

        if ha == hb and A == B: return True
        for i, x in enumerate(A):
            code = ord(x) - 96
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i + 1:] + A[:i + 1] == B:
                return True
        return False
