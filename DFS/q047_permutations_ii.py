# Time:  O(n!)
# Space: O(1)

# 解题思路：
# 一种比较简单的思路是依然全遍历生成，然后利用set特性去重(需先转化为tuple)，思考是否有效率更高的做法，利用组合的特性？
# 计数器维护所有元素，然后递归的方式从中选择元素
# 优化思路：插入到重复元素之前来解决重复的问题


class Solution:
    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_list = list(nums)
        permutations = set()

        def permuteR(permutation):
            if not num_list:
                return

            num_copy = list(num_list)

            for i, num in enumerate(num_copy):
                if len(num_list) == 1:
                    permutations.add(tuple(permutation + [num]))
                    return

                # print(num_list)
                num_list.pop(i)
                # print(num_list)
                # num_list.remove(num)
                permutation.append(num)
                permuteR(permutation)
                num_list.insert(i, num)
                # print(num_list)
                # num_list.append(num)
                permutation.remove(num)

        permuteR([])
        return [list(p) for p in permutations]

    # dfs
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import collections

        if not nums:
            return []

        counter = collections.Counter(nums)
        ans = []

        def permuteR(permutation):
            if not counter:
                ans.append(permutation[:])

            for i in list(counter.keys()):
                counter[i] -= 1
                if counter[i] <= 0:
                    counter.pop(i)

                permutation.append(i)
                permuteR(permutation)
                permutation.pop()
                if i in counter:
                    counter[i] += 1
                else:
                    counter[i] = 1

        permuteR([])
        return ans


# 迭代会快很多
class SolutionF:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        res = [nums[:]]
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                j = n - 1
                while nums[j] <= nums[i - 1]:
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                res.append(nums[:])
                i = n - 1
            else:
                i -= 1

        return res


# 利用set去重
class SolutionF2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = None
        for num in nums:
            if res is None:
                res = {tuple([num])}
            else:
                found = set()
                for p in res:
                    perm = list(p)
                    found.add(tuple(perm + [num]))
                    for i in range(len(perm)):
                        found.add(tuple(perm[:i] + [num] + perm[i:]))

                res = found

        return list(res)


# To find the last index for inserting new number n into old permutation p, I search for previous instances of n in
# p. But because index throws an exception if unsuccessful, I add a sentinel n at the end (which is the appropriate
# last insertion index then).
# 插入到重复元素之前来解决重复的问题
class Solution1:
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]
        return perms

    def permuteUnique1(self, nums):
        from functools import reduce

        return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
                                        for p in perms
                                        for i in range((p + [n]).index(n) + 1)],
                      nums, [[]])
