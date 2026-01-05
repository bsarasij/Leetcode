class Solution:
    def minOperations(self, nums: List[int]) -> int:
        idx = 0
        counter = 0
        while idx < len(nums) - 2:
            if nums[idx] == 0:
                nums[idx] = 1 - nums[idx]
                nums[idx + 1] = 1 - nums[idx + 1]
                nums[idx + 2] = 1 - nums[idx + 2]
                counter += 1
            idx += 1
        return counter if all(x == 1 for x in nums) else -1