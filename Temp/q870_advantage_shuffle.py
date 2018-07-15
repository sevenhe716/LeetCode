# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    # greedy
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)

        a_i = list(zip(A, list(range(n))))
        b_i = list(zip(B, list(range(n))))

        a_i.sort(key=lambda x: x[0])
        b_i.sort(key=lambda x: x[0])

        a_index, b_index = 0, 0
        index = 0

        ans = [0] * n

        last_index = n-1

        while index < n:
            if a_i[a_index][0] > b_i[b_index][0]:
                ans[b_i[b_index][1]] = a_i[a_index][0]
                b_index += 1
                a_index += 1
            else:
                ans[b_i[last_index][1]] = a_i[a_index][0]
                last_index -= 1
                a_index += 1
            index += 1

        return ans
