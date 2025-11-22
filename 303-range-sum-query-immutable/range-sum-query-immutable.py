class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums        
        self.cumsum = [None]*len(nums)
        self.cumsum[0] = nums[0]
        for i in range(1, len(nums)):
            self.cumsum[i] = self.cumsum[i - 1] + nums[i]
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right] - self.cumsum[left] + self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)