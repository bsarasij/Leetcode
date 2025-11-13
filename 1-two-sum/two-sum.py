class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in maps:
                return [i, maps[rem]]
            maps[nums[i]] = i