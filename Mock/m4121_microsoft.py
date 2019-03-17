# Time:  O(n)
# Space: O(1)

# Ideas:
# two pointer


class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        end1, end2, end = m - 1, n - 1, m + n - 1

        # nums1[end1]
        while end1 >= 0 and end2 >= 0:
            if nums1[end1] >= nums2[end2]:
                nums1[end] = nums1[end1]
                end1 -= 1
            else:
                nums1[end] = nums2[end2]
                end2 -= 1
            end -= 1

        while end2 >= 0:
            nums1[end] = nums2[end2]
            end2 -= 1
            end -= 1
