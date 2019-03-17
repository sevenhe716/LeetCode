# Time:  O(n)
# Space: O(1)

# Ideas:
# mark


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> float:
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
