class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum = 0
        n = len(nums)
        min_len = inf
        while r < n:
            sum += nums[r]
            while sum >= target:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l+= 1
                
            r += 1
        return 0 if (min_len == inf) else min_len