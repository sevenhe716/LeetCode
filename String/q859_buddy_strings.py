# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        import collections
        if len(A) < 2 or len(B) < 2:
            return False

        if A == B:
            if max(collections.Counter(A).values()) >= 2:
                return True
            else:
                return False

        if len(A) != len(B):
            return False

        diff = [i for i in range(len(A)) if A[i] != B[i]]

        if len(diff) != 2:
            return False

        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True

        return False
