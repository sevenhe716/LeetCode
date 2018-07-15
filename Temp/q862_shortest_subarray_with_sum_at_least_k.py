# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def shortestSubarray1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        largest = A[0]
        total = 0

        min_count = 2147483647
        cur_count = 0

        for i in range(len(A)):
            total += A[i]
            largest = max(largest, total)

            cur_count += 1

            if largest >= K:
                cur_largest = largest
                # 往前找到最短的区间
                while cur_largest >= K:
                    print(i - cur_count + 1)
                    cur_largest -= A[i - cur_count + 1]
                    cur_count -= 1

                min_count = min(min_count, cur_count + 1)
                cur_count = 0
                total = 0

            if total < 0:
                total = 0
                cur_count = 0

        if largest < K:
            return -1
        else:
            return min_count


    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # largest = A[0]
        largest = 0
        total = 0

        min_count = 2147483647
        cur_count = 0

        for i in range(len(A)):
            total += A[i]
            # largest = max(largest, total)

            cur_count += 1

            if total >= K:
                min_count = min(min_count, cur_count)
                cur_count = 0
                total = 0

            if total < 0:
                total = 0
                cur_count = 0

        if min_count == 2147483647 and total < K:
            return -1

        for i in range(len(A))[::-1]:
            total += A[i]

            cur_count += 1

            if total >= K:
                min_count = min(min_count, cur_count)
                cur_count = 0
                total = 0

            if total < 0:
                total = 0
                cur_count = 0

        return min_count
