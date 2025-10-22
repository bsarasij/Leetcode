class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maps = {}
        max_len = 0
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        for key in maps:
            if key + 1 in maps:
                max_len = max(max_len, maps[key] + maps[key+1])
        return max_len