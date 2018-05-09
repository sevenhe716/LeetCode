# Time:  O(log(m+n))
# Space: O(1)

# 解题思路：
# 有个显而易见的思路是，双指针遍历两个数组，取(m+n)/2的那个元素即可，但是时间复杂度是O(m+n)
# 利用二分查找，先取出两个数组的中位数，较小的那个去除左端min(m, n)/2个元素，较大的那个去除右端min(m, n)/2个元素
# 分治递归直到元素只剩一个或两个
# 需要考虑的特殊情况：
# 1. 当数组长度为偶数，取左中位数
# 2. 某个数组长度已经为0时作为结束条件
# 3. 当某个数组长度为1时需要特殊处理，具体分为二数，三数，四数求中位数
# 4. 当中位数相等时，需要特殊处理

# 解题思路（续）：
# 之前陷入了一个误区，把偶数集合的中位数简化为左中位数，当中位数出现相等的情况时，会出现边界条件问题
# 因此新思路是偶数集合比较两个中位数，奇数集合一个中位数，共有1+1，1+2，2+2三种情况
# 然后比较两个区间的重叠关系，如果是完全包含关系，则成功找到中位数，当出现相等时，也归为重叠
# 如果没有，则跟之前思路一样，去除掉两侧的元素，个数为index
# 去除的规则应比较两个集合对应位置的元素大小

# 解题思路（续续）：
# 根据上面的思路，其实可以不用取出两个集合的中位数，而是取出较短的集合中位数，然后比较m[i], n[i], n[-i-1]，去除掉两端的元素即可
# 每次可以减少min(m+2)/2个元素，所以复杂度是log(m+n)
# 取双中位数比较区间重叠关系的好处是，对于命中条件的集合，可以极大减少运行时间（同时增加了miss的计算成本），这里不予保留
# 还有一个注意点是，奇偶需要分开处理，当长度为奇数时，不能移除中位数本身


class Solution:
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1, len2 = len(nums1), len(nums2)

        while len1 != 0 and len2 != 0:
            if len1 == 1 or len2 == 1:  # 数组长度为1时需要单独处理
                mids = []
                if len1 == 1:
                    nums = nums2
                    mids.append(nums1[0])
                else:
                    nums = nums1
                    mids.append(nums2[0])

                mid = (len(nums) + 1) // 2 - 1

                if len(nums) % 2 == 0:  # 当数组为偶数时，三数求中位数
                    mids.append(nums[mid])
                    mids.append(nums[mid + 1])
                    mids.sort()  # 由于数量较少，简化直接用排序
                    return mids[1]
                else:
                    if len(nums) == 1:  # 当两个数组都只有一个元素时，二者求中位数
                        return (mids[0] + nums[0]) / 2.

                    mids.append(nums[mid])  # 当数组为奇数时，四数求中位数
                    mids.append(nums[mid - 1])
                    mids.append(nums[mid + 1])
                    mids.sort()
                    return (mids[1] + mids[2]) / 2.

            index1 = (len1 + 1) // 2 - 1
            index2 = (len2 + 1) // 2 - 1

            num1 = nums1[index1]
            num2 = nums2[index2]

            count = min(index1, index2)

            if num1 < num2:
                nums1 = nums1[count + 1:]
                nums2 = nums2[:len2 - count - 1]
            elif num1 > num2:
                nums2 = nums2[count + 1:]
                nums1 = nums1[:len1 - count - 1]
            else:  # 当中位数相等时需要特殊处理，直接这2-4个中位数中产生最终的结果
                mids = []
                if len1 % 2 == 1:
                    mids.append(num1)
                else:
                    mids.append(nums1[index1])
                    mids.append(nums1[index1 + 1])

                if len2 % 2 == 1:
                    mids.append(num2)
                else:
                    mids.append(nums2[index2])
                    mids.append(nums2[index2 + 1])

                mids.sort()
                m = (len(mids) + 1) // 2 - 1
                if len(mids) % 2 == 1:
                    return mids[m]
                else:
                    return (mids[m] + mids[m + 1]) / 2.

            len1, len2 = len(nums1), len(nums2)

        # 不可能出现两个slice同时为0，只可能同时为1
        if len1 == 0:
            nums = nums2
        else:
            nums = nums1

        mid = (len(nums) + 1) // 2 - 1

        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid + 1]) / 2.

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1, len2 = len(nums1), len(nums2)

        while len1 > 0 and len2 > 0:
            if len1 == 1 and len2 == 1:
                return (nums1[0] + nums2[0]) / 2.

            index1 = (len1 + 1) // 2 - 1
            index2 = (len2 + 1) // 2 - 1

            # 奇数数组中位数也化归为偶数两个中位数统一处理，但是在后面取中位数时需要单独处理
            if len1 % 2 == 1:
                index_l1 = index1
                index_r1 = index1
            else:
                index_l1 = index1
                index_r1 = index1 + 1

            if len2 % 2 == 1:
                index_l2 = index2
                index_r2 = index2
            else:
                index_l2 = index2
                index_r2 = index2 + 1

            mid_l1 = nums1[index_l1]
            mid_r1 = nums1[index_r1]
            mid_l2 = nums2[index_l2]
            mid_r2 = nums2[index_r2]

            # 判断是否是区间包含关系，如果是则直接找到中位数
            if mid_l1 <= mid_l2 and mid_r1 >= mid_r2 or mid_l2 <= mid_l1 and mid_r2 >= mid_r1:
                if mid_l1 <= mid_l2 and mid_r1 >= mid_r2:
                    mid_l = mid_l2
                    mid_r = mid_r2
                else:
                    mid_l = mid_l1
                    mid_r = mid_r1

                mid_count = 4 - len1 % 2 - len2 % 2  # 1+1, 1+2, 2+1, 2+2
                if mid_count == 2:
                    return mid_l
                elif mid_count == 3:
                    return mid_l
                else:
                    return (mid_l + mid_r) / 2.

            else:
                if mid_l1 <= mid_l2:  # 标记左右集合索引
                    count_l = index_l1 + 1
                else:
                    count_l = index_l2 + 1

                if mid_r1 > mid_r2:
                    count_r = len1 - index_r1
                else:
                    count_r = len2 - index_r2

                del_count = min(count_l, count_r)  # 两侧移除的个数

                s1, e1, s2, e2 = 0, len1, 0, len2

                if nums1[del_count - 1] <= nums2[del_count - 1]:
                    s1 = del_count
                else:
                    s2 = del_count

                if nums1[-del_count] >= nums2[-del_count]:
                    e1 = len1 - del_count
                else:
                    e2 = len2 - del_count

                nums1 = nums1[s1:e1]
                nums2 = nums2[s2:e2]

            len1, len2 = len(nums1), len(nums2)

        # 不可能出现两个slice同时为0，只可能同时为1
        if len1 == 0:
            nums = nums2
        else:
            nums = nums1

        mid = (len(nums) + 1) // 2 - 1

        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid + 1]) / 2.

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)

        # 当其中一个集合已经删除为空时
        if len1 == 0 or len2 == 0:
            if len1 == 0:
                nums = nums2
            else:
                nums = nums1

            mid = (len(nums) + 1) // 2 - 1

            if len(nums) % 2 == 1:
                return nums[mid]
            else:
                return (nums[mid] + nums[mid + 1]) / 2.

        # 当其中一个集合只剩一个元素时
        if len1 == 1 or len2 == 1:
            mids = []
            if len1 == 1:
                nums = nums2
                mids.append(nums1[0])
            else:
                nums = nums1
                mids.append(nums2[0])

            mid = (len(nums) + 1) // 2 - 1

            if len(nums) % 2 == 0:  # 当数组为偶数时，三数求中位数
                mids.append(nums[mid])
                mids.append(nums[mid + 1])
                mids.sort()  # 由于数量较少，简化直接用排序
                return mids[1]
            else:
                if len(nums) == 1:  # 当两个数组都只有一个元素时，二者求中位数
                    return (mids[0] + nums[0]) / 2.

                mids.append(nums[mid])  # 当数组为奇数时，四数求中位数
                mids.append(nums[mid - 1])
                mids.append(nums[mid + 1])
                mids.sort()
                return (mids[1] + mids[2]) / 2.

        # 当两个集合都大于2时，取较小的集合的中位数及索引进行比较
        len_min = min(len1, len2)

        count = (len_min + 1) // 2 - 1 + 1
        offset = len_min % 2  # 分奇偶截取集合，若为奇数不截取中位数

        s1, e1, s2, e2 = 0, len1, 0, len2

        if nums1[count - 1] <= nums2[count - 1]:
            s1 = count - offset
        else:
            s2 = count - offset

        if nums1[-count] >= nums2[-count]:
            e1 = len1 - count + offset
        else:
            e2 = len2 - count + offset

        return self.findMedianSortedArrays(nums1[s1:e1], nums2[s2:e2])

    # 参考答案，分治算法二分查找两个集合中第K个元素
    # 查找两个排序数组中第K小的元素
    # https://articles.leetcode.com/find-k-th-smallest-element-in-union-of/
    # 思路泛化到任意第K个元素，我之前是考虑特化的中位数，所以两端一起裁剪元素

    def findMedianSortedArrays4(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2) // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2) // 2) +
                    self.getKth(nums1, nums2, (len1 + len2) // 2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) // 2
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)

    def findMedianSortedArrays5(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth2([nums1, nums2], (len1 + len2) // 2 + 1)
        else:
            return (self.getKth2([nums1, nums2], (len1 + len2) // 2) +
                    self.getKth2([nums1, nums2], (len1 + len2) // 2 + 1)) * 0.5

    def getKth2(self, arrays, k):
        def binary_search(array, left, right, target, compare):
            while left <= right:
                mid = left + (right - left) // 2
                if compare(array, mid, target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def match(arrays, num, target):
            res = 0
            for array in arrays:
                if array:
                    res += len(array) - binary_search(array, 0, len(array) - 1, num,
                                                      lambda array, x, y: array[x] > y)
            return res < target

        left, right = float("inf"), float("-inf")
        for array in arrays:
            if array:
                left = min(left, array[0])
                right = max(right, array[-1])

        return binary_search(arrays, left, right, k, match)


# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
