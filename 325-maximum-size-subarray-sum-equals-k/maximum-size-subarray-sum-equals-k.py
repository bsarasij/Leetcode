class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        map = {0:-1}
        pref_sum = 0
        max_len = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            if (pref_sum - k) in map:
                max_len = max(max_len, i - map[pref_sum - k])
            if pref_sum not in map:    
                map[pref_sum] = i
        return max_len
