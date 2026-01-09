class Solution:
    def jumpTo(self, i, nums, n, dp):
        if i == n-1:
            return True
        if dp[i] != -1:
            return dp[i]

        for j in range(i+1, min(i+nums[i] + 1, n)):
            if self.jumpTo(j, nums, n, dp):
                dp[i] = 1
                return True
        
        dp[i] = 0
        return False
        
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1 for i in range(len(nums))]
        return self.jumpTo(0, nums, n, dp)