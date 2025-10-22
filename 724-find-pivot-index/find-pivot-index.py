class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = 0
        curr_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
        
        for i in range(len(nums)):
            if pref_sum - nums[i] - curr_sum == curr_sum:
                return i
            curr_sum += nums[i]
        return -1 