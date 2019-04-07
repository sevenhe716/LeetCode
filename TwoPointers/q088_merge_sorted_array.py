# Time:  O(m+n)
# Space: O(1)

# 解题思路：
# 从后往前比较赋值，减少比较和赋值次数，比较次数最多为m+n次，最少为min(m+n)次，赋值次数最多为m+n次，最少为n次，
# 最终如果nums2还有剩余元素，整体赋值给nums1


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if not nums1 or not nums2:
            return

        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1

        # python支持批量赋值
        nums1[:j+1] = nums2[:j+1]
        # if j >= 0:
        #     for x in range(j+1):
        #         nums1[x] = nums2[x]


class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 终止条件为nums2为空，这种写法更简洁，但每次m+n-1计算量稍大
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
