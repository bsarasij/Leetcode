class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = [None for i in range(len(nums))]
        run_sum[0] = nums[0]
        for i in range(1, len(nums)):
            run_sum[i] = run_sum[i-1] + nums[i]
        return list(run_sum)