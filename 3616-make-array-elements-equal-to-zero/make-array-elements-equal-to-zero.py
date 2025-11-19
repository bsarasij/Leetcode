class Solution:
    def simulate(self, nums, curr, init_dir):
        val = init_dir
        while curr < len(nums) and curr >= 0:
            if nums[curr] == 0:
                curr = curr + val
            elif nums[curr] > 0:
                nums[curr] -= 1
                val = - val
                curr += val
        return nums
        
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] == 0:
                for d in [-1,1]:
                    nums_c = nums.copy()
                    nums_c = self.simulate(nums_c, i, d)
                    if all(x == 0 for x in nums_c):
                        count += 1
        return count