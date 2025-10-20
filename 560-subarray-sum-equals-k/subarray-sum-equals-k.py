class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0 : 1}
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if (prefix_sum - k) in map:
                count += map[prefix_sum - k]
            map[prefix_sum] = map.get(prefix_sum,0) + 1
        return count