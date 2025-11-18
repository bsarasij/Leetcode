class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        max_len = 0
        count_zeros = 0
        while r < n:
            if nums[r] == 0:
                count_zeros += 1
            while count_zeros > k:
                if nums[l] == 0:
                    count_zeros -= 1
                l += 1

            if count_zeros <= k:
                max_len = max(max_len, r - l + 1)

            r += 1
        return max_len