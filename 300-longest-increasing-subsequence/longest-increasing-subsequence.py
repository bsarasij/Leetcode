class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        tab = [1]*n
        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    tab[i] = max(tab[i], 1+ tab[j])
        return max(tab)
                
