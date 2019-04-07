# Time:  O(n)
# Space: O(1)

# 解题思路：
# 当前序列是基于上一个序列的，所以只能从1开始生成或者用递归，找到相同连续的数字并计算个数（双指针）


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = 1
        cur_list = [1]

        while cur < n:
            new_list = []
            i, j = 0, 0
            while j < len(cur_list):
                while j < len(cur_list) and cur_list[i] == cur_list[j]:
                    j += 1
                new_list.append(j - i)
                new_list.append(cur_list[i])
                i = j

            cur_list = new_list
            cur += 1

        return ''.join([str(i) for i in cur_list])


class Solution1:
    def countAndSay(self, n):
        result = '1'
        for _ in range(n - 1):
            prev = result
            result, j = '', 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1
                    j += 1
                result += str(cnt) + str(cur)
        return result