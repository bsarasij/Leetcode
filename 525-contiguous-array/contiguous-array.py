class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {0:-1}
        pref_sum = 0
        max_len = 0 
        for i in range(len(nums)):
            pref_sum = pref_sum + (1 if nums[i] == 1 else -1)
            if pref_sum in maps:
                max_len = max(max_len, i - maps[pref_sum])
            else:
                maps[pref_sum] = i
        return max_len
