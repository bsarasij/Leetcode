class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
            if y in maps and maps[y] != i:
                return [i, maps[y]]