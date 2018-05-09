# Time:  O(n^2)
# Space: O(n^2)

# 解题思路：
# 若想降低时间复杂度，可以空间换时间，两数求和的结果存在map中，反向索引，key为两数之和，value为所有的集合，然后查找相反数即可
# 需要注意的是，当元素相同时，需要再进行一次验证，防止相同元素使用次数多于个数，可以用counter
# 优化思路：反向索引map去重
# 优化思路：限定四数的大小顺序，减少重复的概率


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        import collections

        nums.sort()
        nums_counter = collections.Counter(nums)
        two_sum_dict = {}        # 反向索引两数之和
        raw_nums, four_nums = [], []

        for i in range(0, len(nums)-1):
            for j in range(i, len(nums)):
                # 去重
                is_duplicated = False
                for [x, y] in two_sum_dict.setdefault(nums[i] + nums[j], []):
                    if nums[i] == x:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    two_sum_dict.setdefault(nums[i] + nums[j], []).append([nums[i], nums[j]])

        for ts, nl1s in two_sum_dict.items():
            if target - ts in two_sum_dict:
                # 保证四数的顺序
                raw_nums += [nl1 + nl2 for nl1 in nl1s for nl2 in two_sum_dict[target - ts] if nl1[1] <= nl2[0]]

        # 再逐个验证，移除掉使用次数大于个数的元素，以及重复的元素
        for raw_num in raw_nums:
            rnc = collections.Counter(raw_num)

            flag = True
            for rn, c in rnc.items():
                if nums_counter[rn] < c:
                    flag = False
                    break

            if flag:
                four_nums.append(raw_num)

        return four_nums


# Two pointer solution. (1356ms)
class Solution1(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res


# Time:  O(n^2 * p)
# Space: O(n^2 * p)
# Hash solution. (224ms)
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections

        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)  # defaultdict
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:        # 去重
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in range(2, len(nums)):
            for d in range(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:           # 限定a<b<c<d，没有等于吗？？？
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(str(quad))     # 用str来代替list比较，作为hash值
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result


# Time:  O(n^2 * p) ~ O(n^4)
# Space: O(n^2)
class Solution3(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections

        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                           b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)


# 延续的Sum3的思路，只是在外面再加了一层，边界判断会提高不少运行速度
class SolutionF:
    def fourSum(self, nums, target):
        result = []
        N = len(nums)
        if N < 4:
            return result
        nums = sorted(nums)

        if sum(nums[-4:]) < target:
            return result

        for i in range(N - 3):
            if sum(nums[i:i + 4]) > target:                             # 边界判断，提前终止
                break
            if nums[i] + sum(nums[-3:]) < target:                       # 右边界判断
                continue
            if i > 0 and nums[i] == nums[i - 1]:                        # 元素相同则直接跳过（只能跳过i-1）
                continue
            target2 = target - nums[i]
            for j in range(i + 1, N - 2):
                if sum(nums[j:j + 3]) > target2 or sum(nums[-3:]) < target2:
                    break
                if nums[j] + sum(nums[-2:]) < target2:
                    continue
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target3 = target2 - nums[j]
                left = j + 1
                right = N - 1
                while left < right:
                    if nums[left] + nums[right] == target3:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target3:
                        left += 1
                    else:
                        right -= 1
        return result

# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order.
# (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#   A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)
#