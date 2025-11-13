class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                lo += 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        