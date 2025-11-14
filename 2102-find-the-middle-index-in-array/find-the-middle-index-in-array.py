class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        arr_sum = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            if arr_sum - nums[i] - curr_sum == curr_sum:
                return i
            curr_sum += nums[i]
        return -1