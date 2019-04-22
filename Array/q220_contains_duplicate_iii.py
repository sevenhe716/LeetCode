# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: int, t: int) -> bool:
        if t < 0: return False
        lookup = {}
        for i in range(len(nums)):
            b_idx = nums[i] // (t + 1)
            if b_idx in lookup:
                return True
            if b_idx - 1 in lookup and abs(nums[i] - lookup[b_idx - 1]) < t + 1:
                return True
            if b_idx + 1 in lookup and abs(nums[i] - lookup[b_idx + 1]) < t + 1:
                return True
            lookup[b_idx] = nums[i]
            if i >= k: del lookup[nums[i - k] // (t + 1)]
        return False
