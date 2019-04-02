# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 有个思路是，选择一个数，然后用此数减去第二个数，查找第三个数是否在集合中，时间复杂度为O(n^3)
# 另外一个思路是，先把数组排序，三数之和为0，必定是二正一负或二负一正(0单独讨论)
# 然后相加之后取反在数组中查找第三个数即可(因为已经排序，二分查找会将时间复杂度从O(n)降到O(log(n)))
# 而且两数求和遍历会少一半(2*(0.5)n^2)，时间复杂度为O(nlog(n))+O(0.5n^2log(n))
# 一个关键点是，不包含重复的元组，涉及到去重的问题（保证返回的是有序集合，每次添加之前检查集合是否已包含即可）
# 优化思路：若时间复杂度想进一步降低，则只能空间换时间，建个map来减少查找的开销
# 优化思路：利用边界判断来提前终止循环
# 优化思路：in在list很大的时候会很慢，O(n)的时间复杂度，列表尽量不要使用if in
# 优化思路：元素先去重，极大地减少遍历个数，用counter来统计个数
# 优化思路：其实不排序也可以，只要保证第三个数与前两个数的大小关系即可，如mid one


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # from bisect import bisect_left
        #
        # def binary_search_in(a, x):
        #     if x < a[0] or x > a[-1]:
        #         return False
        #     pos = bisect_left(a, x)
        #     return pos < len(a) and a[pos] == x

        import collections

        nums.sort()

        check_negative = True
        check_positive = True
        index_n = 0
        index_p = len(nums)
        zero_count = 0

        results = []

        # 将数组分割成正负两部分，并同时统计0的个数
        for i, num in enumerate(nums):
            if check_negative and num >= 0:
                index_n = i
                check_negative = False
            if check_positive and num > 0:
                index_p = i
                check_positive = False

            if num == 0:
                zero_count += 1

        neg_nums = nums[:index_n]
        pos_nums = nums[index_p:]

        neg_dict = collections.Counter(neg_nums)
        pos_dict = collections.Counter(pos_nums)

        if zero_count > 0:
            if len(pos_nums) > 0:
                neg_pre = 1
                for neg in neg_nums:
                    if neg_pre == neg:
                        continue
                    neg_pre = neg

                    if -neg < pos_nums[0]:
                        break

                    if -neg > pos_nums[-1]:
                        continue

                    if -neg in pos_dict:
                        results.append([neg, 0, -neg])

            if zero_count >= 3:
                results.append([0, 0, 0])

        if len(pos_nums) > 0:
            i_pre = 1
            for i in range(len(neg_nums) - 1, 0, -1):
                if i_pre == neg_nums[i]:  # 跳过重复的元素
                    continue
                i_pre = neg_nums[i]

                if neg_nums[i] + neg_nums[i] + pos_nums[-1] < 0:  # 最大的正数与最大的负数的两倍相加都小于0，则终止循环
                    break

                j_pre = 1
                for j in range(i - 1, -1, -1):
                    if j_pre == neg_nums[j]:  # 跳过重复的元素
                        continue
                    j_pre = neg_nums[j]

                    if neg_nums[i] + neg_nums[0] + pos_nums[0] > 0:  # 最小的负数与最小正数相加都大于0，则终止循环
                        break

                    if neg_nums[i] + neg_nums[j] + pos_nums[-1] < 0:  # 最大的负数与最大的正数相加都小于0，则终止循环
                        break

                    pos_num = - neg_nums[i] - neg_nums[j]
                    # if pos_num in pos_dict and [neg_nums[i], neg_nums[j], pos_num] not in results:  # in的效率很低
                    if pos_num in pos_dict:
                        results.append([neg_nums[i], neg_nums[j], pos_num])

            # for i in range(len(neg_nums) - 1):
            #     if neg_nums[i] + neg_nums[i] + pos_nums[0] > 0:     # 最小的正数与最小的负数的两倍相加都大于0，则终止循环
            #         print("remain1=%d" % (len(neg_nums) - 1 - i))
            #         break
            #
            #     for j in range(i+1, len(neg_nums)):
            #         self.call_count += 1
            #         if neg_nums[i] + neg_nums[j] + pos_nums[0] > 0:     # 最小的负数与最小正数相加都大于0，则终止循环
            #             break
            #
            #         if neg_nums[i] + neg_nums[-1] + pos_nums[-1] < 0:   # 最大的负数与最大的正数相加都小于0，则终止循环
            #             break
            #
            #         call_count2 += 1
            #         pos_num = - neg_nums[i] - neg_nums[j]
            #         if pos_num in pos_dict and [neg_nums[i], neg_nums[j], pos_num] not in results:
            #             results.append([neg_nums[i], neg_nums[j], pos_num])
            #             call_count3 += 1

        if len(neg_nums) > 0:
            i_pre = -1
            for i in range(len(pos_nums) - 1):
                if i_pre == pos_nums[i]:  # 跳过重复的元素
                    continue
                i_pre = pos_nums[i]

                if pos_nums[i] + pos_nums[i] + neg_nums[0] > 0:  # 最大的负数与最小的正数的两倍相加都大于0，则终止循环
                    break

                j_pre = -1
                for j in range(i + 1, len(pos_nums)):
                    if j_pre == pos_nums[j]:  # 跳过重复的元素
                        continue
                    j_pre = pos_nums[j]

                    if pos_nums[i] + pos_nums[j] + neg_nums[0] > 0:  # 最小的正数和最小的负数相加都大于0，则终止循环
                        break

                    if pos_nums[i] + pos_nums[-1] + neg_nums[-1] < 0:  # 最大的正数与最大的负数相加都小于0，则终止循环
                        break

                    neg_num = - pos_nums[i] - pos_nums[j]
                    if neg_num in neg_dict:
                        results.append([neg_num, pos_nums[i], pos_nums[j]])

        return results


class Solution1(object):
    # 先固定第一个数，然后从两端求两数之后，移动两个指针求和，再往中间继续遍历，直到相遇，需要排除相邻元素相等的情况，时间复杂度O(n^2)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0

        if sum(nums[-3:]) < 0:
            return result

        if len(nums) >= 3 and nums[0] == nums[-1] == 0:
            return [[0, 0, 0]]

        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                if sum(nums[i:i+2]) > 0:            # 新增边界判断，用于提前终止提高性能
                    break

                if sum(nums[-2:]) + nums[i] < 0:    # 新增边界判断，用于提前终止提高性能
                    i += 1
                    continue

                j, k = i + 1, len(nums) - 1

                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:             # 相等则继续往中间找
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1

        return result

    # 性能还不如我的算法
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import collections

        d = collections.Counter(nums)
        nums_2 = [x[0] for x in d.items() if x[1] > 1]          # 个数多于1个的元素
        nums_new = sorted([x[0] for x in d.items()])
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_new):
            if j <= 0:
                numss2 = nums_new[i + 1:]
                for x, y in enumerate(numss2):
                    if 0 - j - y in [j, y] and 0 - j - y in nums_2:     # 0-j-y是第三个元素，如果与前两个数相同，则在多于1的数组中找
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
                    if 0 - j - y not in [j, y] and 0 - j - y in nums_new:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn


# 比我快的原因有两点，去重减少元素个数，无需排序
class SolutionF:
    # try to optimize the fastest solution, no sort version
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        import collections

        diction = collections.Counter(nums)
        dict_key = diction.keys()

        pos, neg = [], []
        for p in dict_key:
            if p >= 0:
                pos.append(p)
            else:
                neg.append(p)

        rsts = []

        if diction.get(0, 0) > 2:             # 3-zero condition
            rsts.append([0, 0, 0])
        for p in pos:
            for n in neg:
                inverse = -p - n
                if inverse in diction:
                    # ensure the third one is the mid one
                    if n < inverse < p:
                        rsts.append([n, inverse, p])
                    elif (inverse == p or inverse == n) and diction[inverse] > 1:
                        rsts.append([n, inverse, p])

        return rsts

    # try to optimize the fastest solution, sort version, check bound to break the loop earlier
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        import collections

        diction = collections.Counter(nums)
        dict_key = diction.keys()

        pos, neg = [], []
        for p in dict_key:
            if p >= 0:
                pos.append(p)
            else:
                neg.append(p)

        pos.sort()
        neg.sort()

        rsts = []
        if diction.get(0, 0) > 2:       # 3-zero condition
            rsts.append([0, 0, 0])

        if len(neg) < 1 or len(pos) < 1:
            return rsts

        for p in pos:
            # check bound to break the loop earlier
            if neg[-1] + p + p < 0:
                continue
            if neg[0] + neg[0] + p > 0:
                break

            for n in neg:
                # check bound to break the loop earlier
                if n + n + p > 0:
                    break
                if n + p + p < 0:
                    continue

                inverse = -p - n
                if inverse in dict_key:
                    # ensure the third one is the mid one
                    if n < inverse < p:
                        rsts.append([n, inverse, p])
                    elif (inverse == p or inverse == n) and diction[inverse] > 1:
                        rsts.append([n, inverse, p])

        return rsts

    # 并未提前终止遍历，为什么最快？
    def threeSum(self, nums):
        freq = {}
        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1
        if 0 in freq and freq[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        neg = sorted((filter(lambda x: x < 0, freq)))
        nneg = sorted((filter(lambda x: x >= 0, freq)))
        for elem1 in neg:
            for elem2 in nneg:
                src = -(elem1 + elem2)
                if src in freq:
                    if src in (elem1, elem2) and freq[src] > 1:
                        res.append([elem1, src, elem2])
                    elif src < elem1:
                        res.append([src, elem1, elem2])
                    elif src > elem2:
                        res.append([elem1, elem2, src])
        return res


class SolutionFP:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        diction = {}
        for num in nums:            # 直接使用collections.Counter
            if num in diction:
                diction[num] += 1
            else:
                diction[num] = 1

        dictkey = diction.keys()
        pos, neg = [], []
        for p in dictkey:
            if p >= 0:
                pos.append(p)
            else:
                neg.append(p)

        sorted(pos)                 # 等于是什么事情都没做
        sorted(neg)

        rsts = []
        rst = []                    # 无需提前声明，实际被覆盖
        if 0 in dictkey and diction[0] > 2:
            rsts.append([0, 0, 0])
        pos.reverse()               # 依然等于什么事都没做，依然是乱序
        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in dictkey:
                    if (inverse == p or inverse == n) and diction[inverse] > 1:
                        rst = [inverse, p, n]
                        rsts.append(sorted(rst))        # 既然知道大小关系了，完全没有必要再排序
                    if inverse > p or inverse < n:
                        rst = [inverse, p, n]
                        rsts.append(sorted(rst))

        return rsts
