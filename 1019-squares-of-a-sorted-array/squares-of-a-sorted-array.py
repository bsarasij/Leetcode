class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [x**2 for x in nums]
        n_sorted = [0 for i in range(n)]
        l1 = 0
        l2 = n - 1
        last = n - 1
        while last >= 0:
            if abs(nums[l1]) >= abs(nums[l2]):
                n_sorted[last] = nums[l1]**2
                l1 += 1
            else:
                n_sorted[last] = nums[l2]**2
                l2 -= 1
            last -= 1
        return n_sorted