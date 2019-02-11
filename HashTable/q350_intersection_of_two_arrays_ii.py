# Time:  O(n)
# Space: O(1)

# 解题思路：
# 1. Counter计数器
# 2. 排序后双指针法
# 几个进阶的问题：
# 1. 如果已经排好序了，如何优化？排好序了可以用双指针法
# 2. 如果已经num1比num2小，如何优化？计数器算法则以小数组来遍历
# 3. 如果num2无法在内存中存放，该如何完成算法？计数器算法则可以分块计数，并num2的计数器中移除已匹配的数据
from collections import Counter


class Solution:
    # 算法优化：其实无需两个计数器，维护小数组的计数器即可，匹配成功后移除，跟大数组匹配相同的思路
    def intersect1(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        # 优化：选择从小数组中遍历
        if len(cnt1) > len(cnt2):
            cnt1, cnt2 = cnt2, cnt1
        # res = [[num] * min(cnt1[num], cnt2[num]) for num in cnt1 if num in cnt2]
        res = []
        for num in cnt1:
            if num in cnt2:
                res += [num] * min(cnt1[num], cnt2[num])
        return res

    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        # 优化：选择从小数组中遍历
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        cnt = Counter(nums1)
        res = []
        for num in nums2:
            if num in cnt and cnt[num] > 0:
                res.append(num)
                cnt[num] -= 1
        return res
