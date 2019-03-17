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
