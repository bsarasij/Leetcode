class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        max_k = - inf
        for i in range(len(nums)):
            if nums[i] != 1:
                max_k = max(max_k, k)
                k = 0
            else:
                k += 1
        max_k = max(max_k, k)
        return max_k