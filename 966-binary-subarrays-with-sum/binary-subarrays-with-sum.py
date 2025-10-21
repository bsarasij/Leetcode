class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        map = {0 : 1}
        pref_sum = 0
        count = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            if (pref_sum - goal) in map:
                count += map[pref_sum - goal]
            map[pref_sum] = map.get(pref_sum, 0) + 1
        return count