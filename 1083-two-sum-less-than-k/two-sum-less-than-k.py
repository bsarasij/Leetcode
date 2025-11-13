class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        target = -1
        nums.sort()
        while lo < hi:
            if nums[lo] + nums[hi] < k:
                target = max(target, nums[lo] + nums[hi])
                lo += 1
            else:
                hi -= 1
        return target